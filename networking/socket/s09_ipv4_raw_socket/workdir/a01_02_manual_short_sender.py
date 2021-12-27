"""
Machine A
"""

import socket
import random

import ipv4_utils


def make_message() -> str:
    lipsum = ""
    with open('lipsum.txt', 'r') as lipsum_pf:
        lipsum = "".join(lipsum_pf.readlines())

    AMOUNT = 100
    offset = random.randint(0, len(lipsum) - AMOUNT)
    return lipsum[offset:offset+AMOUNT+1]


def main() -> None:
    print("A START")

    message = make_message()
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
        identification=random.randint(0, 65535 + 1),
        protocol=ipv4_utils.IPPROTO_EXPERIMENTAL_1,
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
