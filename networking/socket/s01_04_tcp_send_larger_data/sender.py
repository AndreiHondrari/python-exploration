import socket
import random


def main() -> None:
    print("START SENDER")

    print("prepare data ...")
    TARGET = 100_000
    data_array = bytearray()
    for _ in range(TARGET):
        data_array.append(random.randint(0, 255))

    data = bytes(data_array)
    DATA_LEN = len(data)

    print("Connect ...")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))

    print("send ...")
    total_sent = 0
    while total_sent < DATA_LEN:
        sent_count = sender.send(data[total_sent:])
        print("amount sent", sent_count)
        total_sent += sent_count

    print("close ...")
    sender.close()

    print("END RECEIVER")


if __name__ == '__main__':
    main()
