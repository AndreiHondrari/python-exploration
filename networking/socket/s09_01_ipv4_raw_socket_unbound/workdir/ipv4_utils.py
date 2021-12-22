
import dataclasses

from typing import Optional

ETH_P_IP = 0x0800  # Internet Protocol packet
IPV4_MAX_PMTU = 65535  # RFC 2675, Section 5.1
IPV4_MIN_MTU = 68  # RFC 791


@dataclasses.dataclass
class IPHeader:
    """
    Length of IP header without options: 128 bits (16 bytes)
    """

    version: int   # 4 bits
    internet_header_length: int  # 4 bits
    differentiated_services_code_point: int  # 6 bits
    explicit_congestion_notification: int  # 2 bits
    total_length: int  # 16 bits (2 bytes)
    identification: int  # 16 bits (2 bytes)
    flags: int  # 3 bits
    fragment_offset: int  # 13 bits
    time_to_live: int  # 8 bits (1 byte)
    protocol: int  # 8 bits (1 byte)
    header_checksum: int  # 16 bits (2 bytes)
    source_ip: bytes  # 32 bits (4 bytes)
    destination_ip: bytes  # 32 bits (4 bytes)
    options: Optional[bytes] = None

    @property
    def source_ip_str(self) -> str:
        return stringify_ip(self.source_ip)

    @property
    def destination_ip_str(self) -> str:
        return stringify_ip(self.destination_ip)


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
    checksum = raw_packet[10]

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

    header_offset: int = 0
    IHL_MIN = 5  # 5 * 32 (bits) = 160 bits = 20 bytes
    if ihl > IHL_MIN:
        header_offset = (ihl * 32) // 8
        options = raw_packet[20:header_offset]
        header.options = options

    return IPPacket(
        header=header,
        payload=raw_packet[header_offset:]
    )
