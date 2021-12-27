"""
Machine A
"""

import socket
import random

import ipv4_utils


def main() -> None:
    print("A START")

    lipsum = ""
    with open('lipsum.txt', 'r') as lipsum_pf:
        lipsum = "".join(lipsum_pf.readlines())

    AMOUNT = 100
    offset = random.randint(0, len(lipsum) - AMOUNT)
    message = lipsum[offset:offset+AMOUNT+1]
    print(f"MSG TO SEND: {message[:50]} ...\n")

    # make sure to encode the message (convert to bytes)
    DATA = message.encode()
    print(f"ENCODED DATA TO SEND: {DATA[:50]!r} ...\n")

    socket_a = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        socket.IPPROTO_RAW
    )

    SOURCE_IP = "172.16.0.2"
    DESTINATION_IP = "172.16.0.3"

    SOURCE_IP_BYTES = socket.inet_aton(SOURCE_IP)
    DESTINATION_IP_BYTES = socket.inet_aton(DESTINATION_IP)

    ip_packet_header = ipv4_utils.IPHeader(
        version=4,
        internet_header_length=5,
        differentiated_services_code_point=0,
        explicit_congestion_notification=0,
        # CAN NOT DETERMINE YET: total_length=total_length,
        identification=random.randint(0, 65535 + 1),
        flags=ipv4_utils.IPV4_FLAG_DO_NOT_FRAGMENT,
        fragment_offset=0,
        time_to_live=64,
        protocol=ipv4_utils.IPPROTO_EXPERIMENTAL_1,
        # CAN NOT DETERMINE YET: header_checksum=checksum,
        source_ip=SOURCE_IP_BYTES,
        destination_ip=DESTINATION_IP_BYTES
    )

    print("Header of packet to send:")
    ipv4_utils.print_ip_packet_header(ip_packet_header)

    ip_packet = ipv4_utils.IPPacket(
        header=ip_packet_header,
        payload=DATA
    )

    ip_header_bytes = ipv4_utils.convert_ip_header(ip_packet)
    header_bytes_chained = ipv4_utils.chain_ip_header_fields(ip_header_bytes)
    packet_bytes_chained = header_bytes_chained + DATA

    socket_a.sendto(
        packet_bytes_chained,
        (DESTINATION_IP, 0,)
    )

    socket_a.close()
    print("\nA STOP")


if __name__ == '__main__':
    main()
