import socket


def main() -> None:
    print("Sender start")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))

    print("sending ...")
    sender.send(b"hello other node!")

    sender.close()
    print("DONE")


if __name__ == '__main__':
    main()
