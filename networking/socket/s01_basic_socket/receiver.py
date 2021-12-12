import socket


def main() -> None:
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    receiver.listen()

    (sender_conn, addr, ) = receiver.accept()

    msg = sender_conn.recv(1024)

    print("RECV", msg)


if __name__ == '__main__':
    main()
