import struct


def main() -> None:
    FORMAT = "@icc?f"
    print("used format:", FORMAT)

    arguments = [257, b'\xf3', 'z'.encode(), True, 55.67]
    print("arguments:", arguments)
    encoded_message = struct.pack(FORMAT, *arguments)
    print("encoded  :", encoded_message)

    decoded_message = struct.unpack(FORMAT, encoded_message)
    print("decoded  :", decoded_message)


if __name__ == '__main__':
    main()
