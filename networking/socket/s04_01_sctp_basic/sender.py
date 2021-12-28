import socket


def main() -> None:
    print("Sender start")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
        socket.IPPROTO_SCTP,
    )

    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))

    print("sending ...")
    sender.send(b"hello other node!")

    print("Wait for reply ...")
    reply = sender.recv(1024)
    print("REPLY:", reply)

    sender.close()
    print("DONE")


if __name__ == '__main__':
    main()
