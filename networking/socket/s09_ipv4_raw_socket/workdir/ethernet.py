from typing import Tuple


def construct_simple_eth_frame(
    destination_mac_address: bytes,
    source_mac_address: bytes,
    ether_type: bytes,
    data: bytes,
) -> bytes:
    # initialize frame
    frame = b''
    frame += destination_mac_address
    frame += source_mac_address
    frame += ether_type
    frame += data

    return frame


def deconstruct_simple_eth_frame(
    frame: bytes
) -> Tuple[bytes, bytes, bytes, bytes]:
    START_DEST = 0
    END_DEST = 5
    START_SRC = 6
    END_SRC = 11
    START_ETH_TYPE = 12
    END_ETH_TYPE = 13
    START_DATA = 14

    destination_mac_address = frame[START_DEST:END_DEST+1]
    source_mac_address = frame[START_SRC:END_SRC+1]
    ether_type = frame[START_ETH_TYPE:END_ETH_TYPE+1]
    data = frame[START_DATA:]

    return destination_mac_address, source_mac_address, ether_type, data
