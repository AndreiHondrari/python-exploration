

def mac_string_to_bytes(address: str) -> bytes:
    mac_elements = address.split(":")
    mac_numbers = [int(x, base=16) for x in mac_elements]
    return bytes(mac_numbers)


def mac_bytes_to_string(address_bytes: bytes) -> str:
    mac_str_elements = [f"{x:0>2x}" for x in address_bytes]
    return ":".join(mac_str_elements)


if __name__ == '__main__':
    x = "02:42:ac:10:00:07"
    k = mac_string_to_bytes(x)
    print("BYTES", k)

    z = mac_bytes_to_string(k)
    print("RECONV", z)
