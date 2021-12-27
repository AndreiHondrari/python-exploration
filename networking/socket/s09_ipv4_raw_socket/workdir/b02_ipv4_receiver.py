"""
Machine B - Receiver
-----–--------------

Receives only IPv4 packet frames.
Does not contain any information about Ethernet frames.

Must specify protocol defined in the sender packet.
In our case it is IPPROTO_EXPERIMENTAL_1 = 253.
"""
import socket
from datetime import datetime

import ipv4_utils

from binary_utils import bytes_hex_stringify


def main() -> None:
    print("B START")
    socket_b = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        ipv4_utils.IPPROTO_EXPERIMENTAL_1  # notice that we have to specify
    )

    print("WAIT RECV ...")
    try:
        while True:
            raw_ip_packet = socket_b.recv(ipv4_utils.IPV4_MAX_PMTU)
            moment = datetime.today().isoformat()

            print()
            print("-" * 10)
            print("RECV", moment)

            print("RAW PACKET:", raw_ip_packet)
            print("PACKET HEX REP:", bytes_hex_stringify(raw_ip_packet))

            ip_packet = ipv4_utils.deconstruct_ipv4_packet(
                raw_ip_packet
            )

            print("IP Header")
            ipv4_utils.print_ip_packet_header(ip_packet.header)

            print("Payload", ip_packet.payload)

    except KeyboardInterrupt:
        print("\nCtrl+c detected")

    socket_b.close()

    print("B STOP")


if __name__ == '__main__':
    main()
