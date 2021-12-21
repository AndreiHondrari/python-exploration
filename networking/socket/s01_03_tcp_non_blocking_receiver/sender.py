import time
import socket
import random


def main() -> None:
    print("START SENDER")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    print("Connect ...")
    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))

    print("wait ...")
    time.sleep(2)

    print("send ...")
    sender.send(f"{random.randint(1000, 10_000)}".encode())

    print("close ...")
    sender.close()

    print("END RECEIVER")


if __name__ == '__main__':
    main()
