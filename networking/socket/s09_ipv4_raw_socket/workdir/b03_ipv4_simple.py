"""
Machine B - Receiver
-----–--------------

Simple receiver. Prints minimum amount of information.
Assumes payload is TEXT.
"""
import socket
from datetime import datetime

import ipv4_utils


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
            print("-" * 10, "RECV", moment)

            ip_packet = ipv4_utils.deconstruct_ipv4_packet(raw_ip_packet)
            print(
                ipv4_utils.stringify_ip(ip_packet.header.source_ip),
                " -> ",
                ipv4_utils.stringify_ip(ip_packet.header.destination_ip),
            )
            print(ip_packet.payload.decode())

    except KeyboardInterrupt:
        print("\nCtrl+c detected")

    socket_b.close()

    print("B STOP")


if __name__ == '__main__':
    main()
