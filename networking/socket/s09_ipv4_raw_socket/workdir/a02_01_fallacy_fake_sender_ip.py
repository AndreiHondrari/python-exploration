"""
Machine A - Sender
------------------


"""
import random
import socket
import functools

import ipv4_utils
from ipv4_utils import simple_construct


hprint = functools.partial(print, "\n\b#")


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
    hprint("MSG TO SEND")
    print(f"{message[:50]} ...")

    # make sure to encode the message (convert to bytes)
    DATA = message.encode()
    hprint("ENCODED DATA TO SEND")
    print(f"{DATA[:50]!r} ...")

    # create socket
    socket_a = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        socket.IPPROTO_RAW
    )

    # important to enable IP_HDRINCL with IPPROTO_NONE
    # IP_HDRINCL will ensure the total_length and checksum are calculated
    socket_a.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    FAKE_SOURCE_IP = "192.168.100.179"
    DESTINATION_IP = "172.16.0.3"

    FAKE_SOURCE_IP_BYTES = socket.inet_aton(FAKE_SOURCE_IP)
    DESTINATION_IP_BYTES = socket.inet_aton(DESTINATION_IP)

    # create IP packet_header
    ip_packet_header = ipv4_utils.IPHeader(
        identification=random.randint(0, 65535 + 1),
        protocol=ipv4_utils.IPPROTO_EXPERIMENTAL_1,
        source_ip=FAKE_SOURCE_IP_BYTES,
        destination_ip=DESTINATION_IP_BYTES
    )

    hprint("Header of packet to send")
    ipv4_utils.print_simple_ip_packet_header(ip_packet_header)

    ip_packet = ipv4_utils.IPPacket(
        header=ip_packet_header,
        payload=DATA
    )

    # encode IP packet
    encoded_ip_packet = simple_construct(ip_packet)
    hprint("Encoded IP packet")
    print(f"{encoded_ip_packet!r}")

    # send
    socket_a.sendto(
        encoded_ip_packet,
        (DESTINATION_IP, 0,)
    )

    socket_a.close()
    print("\nA STOP")


if __name__ == '__main__':
    main()
