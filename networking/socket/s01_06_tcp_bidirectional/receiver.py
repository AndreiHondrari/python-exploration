import socket


def main() -> None:
    print("Receiver start")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    # make sure that we can rebind without TIME_WAIT expiring
    receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    receiver.listen()

    (sender_conn, addr, ) = receiver.accept()

    # the socket created with the accept method is the way to communicate
    msg = sender_conn.recv(1024)

    sender_conn.send(b"Hello to you too!")

    if sender_conn.fileno() > 0:
        sender_conn.close()
    receiver.close()

    print("RECV", msg)


if __name__ == '__main__':
    main()
