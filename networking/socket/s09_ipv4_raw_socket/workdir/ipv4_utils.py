
import dataclasses
import socket
import functools
import struct

from typing import Optional, Dict, Tuple, cast


IPV4_MAX_PMTU = 65535       # RFC 2675, Section 5.1
IPV4_MIN_MTU = 68           # RFC 791

IPV4_FLAG_DO_NOT_FRAGMENT = 0b010
IPV4_FLAG_MORE_FRAGMENTS = 0b001

IPPROTO_EXPERIMENTAL_1 = 253


@functools.cache
def get_ipproto_map() -> Dict[int, str]:
    """
    Maps IPPROTO values to names
    """
    protocol_names = [
        name for name in dir(socket)
        if name.startswith('IPPROTO')
    ]
    protocols = {
        getattr(socket, name): name
        for name in protocol_names
    }

    return protocols


@dataclasses.dataclass
class IPHeader:
    """
    Length of IP header without options: 128 bits (16 bytes)
    """

    identification: int  # 16 bits (2 bytes)
    protocol: int  # 8 bits (1 byte)
    source_ip: bytes  # 32 bits (4 bytes)
    destination_ip: bytes  # 32 bits (4 bytes)

    version: int = 4  # 4 bits
    internet_header_length: int = 5  # 4 bits
    differentiated_services_code_point: int = 0  # 6 bits
    explicit_congestion_notification: int = 0  # 2 bits
    flags: int = IPV4_FLAG_DO_NOT_FRAGMENT  # 3 bits
    fragment_offset: int = 0  # 13 bits
    time_to_live: int = 64  # 8 bits (1 byte)

    header_checksum: Optional[int] = None  # 16 bits (2 bytes)
    total_length: Optional[int] = None  # 16 bits (2 bytes)
    options: Optional[bytes] = None

    @property
    def source_ip_str(self) -> str:
        return stringify_ip(self.source_ip)

    @property
    def destination_ip_str(self) -> str:
        return stringify_ip(self.destination_ip)

    @property
    def protocol_str(self) -> str:
        return get_ipproto_map().get(
            self.protocol,
            f"N/A protocol name ({self.protocol})"
        )


@dataclasses.dataclass
class IPPacket:
    header: IPHeader
    payload: bytes


def stringify_ip(raw_ip: bytes) -> str:
    assert len(raw_ip) == 4
    return ".".join([str(x) for x in raw_ip])


def deconstruct_ipv4_packet(raw_packet: bytes) -> IPPacket:
    # version and IHL
    version_ihl_raw: int = raw_packet[0]
    version = version_ihl_raw >> 4
    ihl = version_ihl_raw & 0x0F

    # DSCP and ECN
    dscp_ecn_raw: int = raw_packet[1]
    dscp = dscp_ecn_raw >> 3
    ecn = dscp_ecn_raw & 0x07

    # Total length of the packet
    total_length: int = int.from_bytes(raw_packet[2:4], 'big')

    # Identification
    identification: int = int.from_bytes(raw_packet[4:6], 'big')

    # Flags and fragment offset
    flags_fragment_raw: int = int.from_bytes(raw_packet[6:8], 'big')
    flags = flags_fragment_raw >> 13
    fragment_offset = flags_fragment_raw & 0x1FFF

    # Time to live
    ttl: int = raw_packet[8]

    # Protocol
    protocol: int = raw_packet[9]

    # Header checksum
    checksum = int.from_bytes(raw_packet[10:12], 'big')

    # Source IP
    source_ip = raw_packet[12:16]

    # Destination IP
    destination_ip = raw_packet[16:20]

    header = IPHeader(
        version=version,
        internet_header_length=ihl,
        differentiated_services_code_point=dscp,
        explicit_congestion_notification=ecn,
        total_length=total_length,
        identification=identification,
        flags=flags,
        fragment_offset=fragment_offset,
        time_to_live=ttl,
        protocol=protocol,
        header_checksum=checksum,
        source_ip=source_ip,
        destination_ip=destination_ip
    )

    IHL_MIN = 5  # 5 * 32 (bits) = 160 bits = 20 bytes
    IHL_MIN_BYTES = (IHL_MIN * 32) // 8

    header_offset: int = IHL_MIN_BYTES
    if ihl > IHL_MIN:
        header_offset = (ihl * 32) // 8
        options = raw_packet[IHL_MIN_BYTES:header_offset]
        header.options = options

    return IPPacket(
        header=header,
        payload=raw_packet[header_offset:]
    )


@dataclasses.dataclass
class IPHeaderBytes:
    version_ihl: bytes  # 1 byte
    dscp_ecn: bytes  # 1 byte
    identification: bytes  # 2 bytes
    flags_and_fragment_offset: bytes  # 2 bytes
    ttl: bytes  # 1 byte
    protocol: bytes  # 1 byte
    source_ip: bytes  # 4 bytes
    destination_ip: bytes  # 4 bytes

    total_length: Optional[bytes] = None  # 2 bytes
    header_checksum: Optional[bytes] = None  # 2 bytes


def combine_version_ihl(version: int, internet_header_length: int) -> int:
    return version << 4 | internet_header_length


def combine_dscp_ecn(dscp: int, ecn: int) -> int:
    return dscp << 3 | ecn


def combine_flags_fragment_offset(flags: int, fragment_offset: int) -> int:
    return flags << 13 | fragment_offset


def preconstruct_ip_header(ip_header: IPHeader) -> IPHeaderBytes:
    """
    Turns all the fields of the ip packet header into bytes.
    Excludes checksum and total length.
    """

    h = ip_header

    return IPHeaderBytes(
        version_ihl=combine_version_ihl(
            h.version,
            h.internet_header_length
        ).to_bytes(1, 'big'),

        dscp_ecn=combine_dscp_ecn(
            h.differentiated_services_code_point,
            h.explicit_congestion_notification
        ).to_bytes(1, 'big'),

        identification=h.identification.to_bytes(2, 'big'),

        flags_and_fragment_offset=combine_flags_fragment_offset(
            h.flags,
            h.fragment_offset
        ).to_bytes(2, 'big'),

        ttl=h.time_to_live.to_bytes(1, 'big'),
        protocol=h.protocol.to_bytes(1, 'big'),
        source_ip=h.source_ip,
        destination_ip=h.destination_ip
    )


def calculate_total_length(ip_packet: IPPacket) -> int:
    """
    Sum of:
        - minimum header size: 20 bytes
        - size of the options bytes: depends on IHL
        - size of the payload
    """

    DEFAULT_HEADER_SIZE = 20  # in bytes
    return sum([
        DEFAULT_HEADER_SIZE,
        abs(5 - ip_packet.header.internet_header_length),
        len(ip_packet.payload)
    ])


def calculate_header_checksum(header_bytes: IPHeaderBytes) -> int:
    assert header_bytes.total_length is not None

    header_bytes_chained = (
        header_bytes.version_ihl +
        header_bytes.dscp_ecn +
        header_bytes.total_length +
        header_bytes.identification +
        header_bytes.flags_and_fragment_offset +
        header_bytes.ttl +
        header_bytes.protocol +
        header_bytes.source_ip +
        header_bytes.destination_ip
    )

    result = sum(
        [x for x in header_bytes_chained]
    )

    while True:
        carry = result >> 16
        if carry == 0:
            break

    result = (0xFFFF & result) + carry

    return 0xFFFF & ~result


def convert_ip_header(
    ip_packet: IPPacket
) -> IPHeaderBytes:

    header_bytes: IPHeaderBytes = preconstruct_ip_header(ip_packet.header)

    # put total length bytes
    total_length = calculate_total_length(ip_packet)
    header_bytes.total_length = total_length.to_bytes(2, 'big')

    # put checksum bytes
    header_checksum = calculate_header_checksum(header_bytes)
    header_bytes.header_checksum = header_checksum.to_bytes(2, 'big')

    return header_bytes


def chain_ip_header_fields(header_bytes: IPHeaderBytes) -> bytes:
    return (
        header_bytes.version_ihl +
        header_bytes.dscp_ecn +
        cast(bytes, header_bytes.total_length) +
        header_bytes.identification +
        header_bytes.flags_and_fragment_offset +
        header_bytes.ttl +
        header_bytes.protocol +
        cast(bytes, header_bytes.header_checksum) +
        header_bytes.source_ip +
        header_bytes.destination_ip
    )


def determine_flags(flags: int) -> Tuple[str, ...]:
    str_flags = []

    if flags & IPV4_FLAG_DO_NOT_FRAGMENT:
        str_flags.append("DO_NOT_FRAGMENT")

    if flags & IPV4_FLAG_MORE_FRAGMENTS:
        str_flags.append("MORE_FRAGMENT")

    return tuple(str_flags)


def print_ip_packet_header(packet_header: IPHeader) -> None:
    print("Source IP:", packet_header.source_ip_str)
    print("Destination IP:", packet_header.destination_ip_str)
    print("Protocol:", packet_header.protocol_str)

    print("Version:", packet_header.version)
    print("IHL:", packet_header.internet_header_length)
    print("DSCP:", packet_header.differentiated_services_code_point)
    print("ECN:", packet_header.explicit_congestion_notification)
    print("Total length:", packet_header.total_length)
    print("Identification:", packet_header.identification)
    print("Flags:", " ".join(determine_flags(packet_header.flags)))
    print("Fragment offset:", packet_header.fragment_offset)
    print("TTL:", packet_header.time_to_live)
    print("Header checksum:", packet_header.header_checksum)
    print("Options:", packet_header.options)


def print_simple_ip_packet_header(packet_header: IPHeader) -> None:
    print("Source IP:", packet_header.source_ip_str)
    print("Destination IP:", packet_header.destination_ip_str)
    print("Protocol:", packet_header.protocol_str)
    print("Identification:", packet_header.identification)


# IP_PACK_STRUCT_FORMAT = "!bb2b2b2bbb2b4b4b"
IP_PACKET_HEADER_STRUCT_FORMAT = "!BBHHHBBH4s4s"


def simple_construct(ip_packet: IPPacket) -> bytes:
    """
    1 byte = version + ihl
    1 byte = dscp + ecn
    2 bytes = total length
    2 bytes = Identification
    2 bytes = flags + fragment offset
    1 byte = ttl
    1 byte = protocol
    2 bytes = checksum
    4 bytes = source IP
    4 bytes = destination IP
    ihl > 5 bytes = options
    """

    h = ip_packet.header

    version_ihl = combine_version_ihl(h.version, h.internet_header_length)
    dscp_ecn = combine_dscp_ecn(
        h.differentiated_services_code_point,
        h.explicit_congestion_notification
    )

    # total_length = calculate_total_length(ip_packet)

    flags_fragment_offset = combine_flags_fragment_offset(
        h.flags,
        h.fragment_offset
    )

    # "!B B H H H B B H 4s 4s"
    ip_packet_header_tuple = (
        version_ihl,  # B
        dscp_ecn,  # B
        0,  # H
        h.identification,  # H
        flags_fragment_offset,  # H
        h.time_to_live,  # B
        h.protocol,  # B
        0,  # H
        h.source_ip,  # 4s
        h.destination_ip,  # 4s
        # h.options if h.options is not None else b'',
    )

    ip_header_bytes = struct.pack(
        IP_PACKET_HEADER_STRUCT_FORMAT,
        *ip_packet_header_tuple
    )

    return (
        ip_header_bytes +
        (h.options if h.options is not None else b'') +
        ip_packet.payload
    )


if __name__ == '__main__':
    import random

    print("\n---CONVERT TO BYTES ---")
    ip_packet_header = IPHeader(
        version=4,
        internet_header_length=5,
        differentiated_services_code_point=0,
        explicit_congestion_notification=0,
        identification=random.randint(0, 65535 + 1),
        flags=IPV4_FLAG_DO_NOT_FRAGMENT,
        fragment_offset=0,
        time_to_live=64,
        protocol=socket.IPPROTO_EGP,
        source_ip=socket.inet_aton("192.168.5.100"),
        destination_ip=socket.inet_aton("192.168.5.100")
    )

    ip_packet = IPPacket(header=ip_packet_header, payload=b'\x11\x22')

    hbytes = convert_ip_header(ip_packet)
    print("HBYTES", hbytes)

    ip_header_bytes = convert_ip_header(ip_packet)
    header_bytes_chained = chain_ip_header_fields(ip_header_bytes)

    print("HBC", header_bytes_chained)
    encoded_ip_packet = header_bytes_chained + ip_packet.payload

    print("\n\n--- DECODE TO IP PACKET STRUCTURE ---")
    decoded_ip_packet = deconstruct_ipv4_packet(encoded_ip_packet)

    print_ip_packet_header(decoded_ip_packet.header)
    print("Payload:", decoded_ip_packet.payload)
