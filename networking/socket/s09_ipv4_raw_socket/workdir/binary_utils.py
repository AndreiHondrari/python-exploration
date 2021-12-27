from typing import List


def bytes_to_hex_list(
    data: bytes
) -> List[str]:
    return [f"{x:0>2x}" for x in data]


def bytes_hex_stringify(
    data: bytes,
    separator: str = ' '
) -> str:
    hex_list: List[str] = bytes_to_hex_list(data)
    return separator.join(hex_list)
