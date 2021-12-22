"""
Machine A
"""

import socket
import random

import ipv4_utils


def main() -> None:
    print("A START")

    # print("DEST MAC ADDR:", TARGET_MAC_ADDRESS_BYTES)
    # print("SRC  MAC ADDR", CURRENT_MAC_ADDRESS, "\n")

    lipsum = ""
    with open('lipsum.txt', 'r') as lipsum_pf:
        lipsum = "".join(lipsum_pf.readlines())

    message = "".join(random.sample(lipsum, 50))
    print(f"MSG TO SEND: {message[:50]} ...\n")

    # make sure to encode the message (convert to bytes)
    data = message.encode()

    # trim to the Ethernet maximum allowed paylod length
    # trimmed_data = data[:ethc.ETH_DATA_LEN]
    # DATA = trimmed_data
    DATA = data

    print(f"ENCODED DATA TO SEND: {DATA[:50]!r} ...\n")

    socket_a = socket.socket(
        socket.AF_INET,
        socket.SOCK_RAW,
        socket.htons(ipv4_utils.ETH_P_IP),
    )
    socket_a.connect(("172.16.0.3", 5555,))
    socket_a.sendall(DATA)

    # print("ETHERNET FRAME TO SEND:", frame)
    # socket_a.sendall(frame)

    socket_a.close()
    print("\nA STOP")


if __name__ == '__main__':
    main()
