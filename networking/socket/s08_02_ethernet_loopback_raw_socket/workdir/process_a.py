"""
Machine A
"""

import uuid
import socket
import random

import ethernet_constants as ethc

import ethernet as eth


def main() -> None:
    print("A START")

    NULL_MAC_ADDRESS = b'\x00' * 6

    lipsum = ""
    with open('lipsum.txt', 'r') as lipsum_pf:
        lipsum = "".join(lipsum_pf.readlines())

    message = "".join(random.sample(lipsum, 50))
    print(f"MSG TO SEND: {message[:50]} ...\n")

    # make sure to encode the message (convert to bytes)
    data = message.encode()

    # trim to the Ethernet maximum allowed paylod length
    trimmed_data = data[:ethc.ETH_DATA_LEN]
    DATA = trimmed_data

    print(f"ENCODED DATA TO SEND: {DATA[:50]!r} ...\n")

    ether_type = ethc.ETH_P_LOOP.to_bytes(2, 'big')
    frame = eth.construct_simple_eth_frame(
        NULL_MAC_ADDRESS,
        NULL_MAC_ADDRESS,
        ether_type,
        DATA
    )

    socket_a = socket.socket(
        socket.AF_PACKET,  # type: ignore[attr-defined]
        socket.SOCK_RAW,
        socket.htons(ethc.ETH_P_ALL),
    )
    socket_a.bind(('lo', 0,))

    print("ETHERNET FRAME TO SEND:", frame)
    socket_a.sendall(frame)

    socket_a.close()
    print("\nA STOP")


if __name__ == '__main__':
    main()
