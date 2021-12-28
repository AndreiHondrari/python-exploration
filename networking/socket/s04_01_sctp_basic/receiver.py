import socket


def main() -> None:
    print("Receiver start")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
        socket.IPPROTO_SCTP,
    )

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    receiver.listen()

    (sender_conn, addr, ) = receiver.accept()

    # get something
    msg = sender_conn.recv(1024)

    # reply to it
    sender_conn.send(b"I got your message !")

    if sender_conn.fileno() > 0:
        sender_conn.close()
    receiver.close()

    print("RECV", msg)


if __name__ == '__main__':
    main()
