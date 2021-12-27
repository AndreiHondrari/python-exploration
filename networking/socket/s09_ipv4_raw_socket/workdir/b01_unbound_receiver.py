"""
Machine B - Receiver
-----–--------------

Unbound because it is not tied to the IP protocol
"""
import socket
from datetime import datetime

import ethernet_constants as ethc
import ethernet as eth
from mac_utils import mac_bytes_to_string as mac_stringify

import ipv4_utils

from binary_utils import bytes_hex_stringify


def main() -> None:
    print("B START")
    socket_b = socket.socket(
        socket.AF_PACKET,  # type: ignore[attr-defined]
        socket.SOCK_RAW,
        socket.htons(ethc.ETH_P_IP),
    )
    socket_b.bind(('eth0', 0,))

    print("WAIT RECV ...")
    try:
        while True:
            frame = socket_b.recv(ipv4_utils.IPV4_MAX_PMTU)
            moment = datetime.today().isoformat()

            print()
            print("-" * 10)
            print("RECV", moment)

            print("FRAME HEX REP", bytes_hex_stringify(frame))

            (
                dst, source, ether_type, data,
            ) = eth.deconstruct_simple_eth_frame(frame)

            print("TO  ", mac_stringify(dst))
            print("FROM", mac_stringify(source))
            print("ETHER TYPE", ether_type)
            print("ETH_P_IP?", ether_type == ethc.ETH_P_IP.to_bytes(2, 'big'))
            print("RAW DATA", data)
            print("DATA HEX REP", bytes_hex_stringify(data))

            raw_ip_packet = data
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
