import struct


def main() -> None:
    string_value = "abcdefgh"
    string_bytes = string_value.encode()
    arguments = [11_123, string_bytes, 99_786]
    print("arguments:", arguments)

    format = f"@I{len(string_bytes)}sl"
    print("used format:", format)

    encoded_message = struct.pack(format, *arguments)
    print("encoded  :", encoded_message)

    decoded_message = struct.unpack(format, encoded_message)
    print("decoded  :", decoded_message)


if __name__ == '__main__':
    main()
