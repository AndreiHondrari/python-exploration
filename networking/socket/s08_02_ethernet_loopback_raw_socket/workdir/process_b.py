"""
Machine B
"""
import socket
from datetime import datetime

import ethernet_constants as ethc
import ethernet as eth
from mac_utils import mac_bytes_to_string as mac_stringify

ETH_FRAME_LEN = 1514  # Max. octets in frame sans FCS


def main() -> None:
    print("B START")
    socket_b = socket.socket(
        socket.AF_PACKET,  # type: ignore[attr-defined]
        socket.SOCK_RAW,
        socket.htons(ethc.ETH_P_ALL),
    )
    socket_b.bind(('lo', 0,))

    print("WAIT RECV ...")
    try:
        while True:
            frame = socket_b.recv(ethc.ETH_FRAME_LEN)
            moment = datetime.today().isoformat()
            print("\n", "-" * 10)
            print("RECV", moment)
            print("FRAME", frame)

            (
                dst, source, ether_type, data,
            ) = eth.deconstruct_simple_eth_frame(frame)

            print("TO  ", mac_stringify(dst))
            print("FROM", mac_stringify(source))
            print("DATA", data)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    socket_b.close()

    print("B STOP")


if __name__ == '__main__':
    main()
