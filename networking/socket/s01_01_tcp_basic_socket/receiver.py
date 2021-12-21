import socket
import errno


def main() -> None:
    print("Receiver start")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    receiver.listen()

    (sender_conn, addr, ) = receiver.accept()

    # receiver socket is used only for acquiring new connectiobs
    try:
        receiver.recv(1024)
    except OSError as oerr:
        print(
            "Caught (intentionally)",
            str(oerr),
            errno.errorcode[oerr.errno]
        )

    # the socket created with the accept method is the way to communicate
    msg = sender_conn.recv(1024)

    if sender_conn.fileno() > 0:
        sender_conn.close()
    receiver.close()

    print("RECV", msg)


if __name__ == '__main__':
    main()
