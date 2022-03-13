import socket
import errno

from typing import Optional


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

    sender_conn: Optional[socket.socket] = None

    try:
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

        print("RECV", msg)
    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Cleaning ...")
        if sender_conn is not None and sender_conn.fileno() > 0:
            sender_conn.close()

        receiver.close()

    print("STOP")


if __name__ == '__main__':
    main()
