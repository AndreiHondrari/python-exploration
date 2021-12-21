import socket


def main() -> None:
    print("\nSENDER START")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))

    print("sending ...")
    sender.send(b"hello other node!")

    sender.close()
    print("SENDER END")


if __name__ == '__main__':
    main()
