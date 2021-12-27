"""
Machine A
"""

import uuid
import socket
import random

import ethernet_constants as ethc
from mac_utils import mac_string_to_bytes as mac_convert

import ethernet as eth


def main() -> None:
    print("A START")
    TARGET_MAC_ADDRESS = "02:42:ac:10:00:09"
    TARGET_MAC_ADDRESS_BYTES = mac_convert(TARGET_MAC_ADDRESS)
    CURRENT_MAC_ADDRESS = uuid.getnode().to_bytes(6, 'big')

    print("DEST MAC ADDR:", TARGET_MAC_ADDRESS_BYTES)
    print("SRC  MAC ADDR", CURRENT_MAC_ADDRESS, "\n")

    lipsum = ""
    with open('lipsum.txt', 'r') as lipsum_pf:
        lipsum = "".join(lipsum_pf.readlines())

    AMOUNT = 100
    offset = random.randint(0, len(lipsum) - AMOUNT)
    message = lipsum[offset:offset+AMOUNT+1]
    print(f"MSG TO SEND: {message[:50]} ...\n")

    # make sure to encode the message (convert to bytes)
    data = message.encode()

    # trim to the Ethernet maximum allowed paylod length
    trimmed_data = data[:ethc.ETH_DATA_LEN]
    DATA = trimmed_data

    print(f"ENCODED DATA TO SEND: {DATA[:50]!r} ...\n")

    ether_type = ethc.ETH_P_802_3.to_bytes(2, 'big')
    frame = eth.construct_simple_eth_frame(
        TARGET_MAC_ADDRESS_BYTES,
        CURRENT_MAC_ADDRESS,
        ether_type,
        DATA
    )

    socket_a = socket.socket(
        socket.AF_PACKET,  # type: ignore[attr-defined]
        socket.SOCK_RAW,
        socket.htons(ethc.ETH_P_ALL),
    )
    socket_a.bind(('eth0', 0,))

    print("ETHERNET FRAME TO SEND:", frame)
    socket_a.sendall(frame)

    socket_a.close()
    print("\nA STOP")


if __name__ == '__main__':
    main()
