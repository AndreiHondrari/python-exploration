import struct
from collections import namedtuple


SomeRecord = namedtuple("SomeRecord", ['a', 'b'])


def main() -> None:
    record = SomeRecord(11, 22)
    print("record :", record)

    FORMAT = "@ii"
    print("format :", FORMAT)

    encoded_record = struct.pack(FORMAT, *record)
    print("encoded:", encoded_record)

    decoded_tuple = struct.unpack(FORMAT, encoded_record)
    decoded_record = SomeRecord._make(decoded_tuple)
    print("decoded:", decoded_record)


if __name__ == '__main__':
    main()
