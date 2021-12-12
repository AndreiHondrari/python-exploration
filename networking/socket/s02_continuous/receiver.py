import time
import socket

from typing import Tuple


def main() -> None:
    print("RECEIVER START")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    print("blocking receiver?", receiver.getblocking())
    receiver.listen()

    try:
        # wait for a connection
        while True:
            print("wait for accept ...")
            sender_conn: socket.socket
            addr: Tuple[str, int]
            (sender_conn, addr,) = receiver.accept()
            print(f"accepted! ({addr})")
            print("blocking sender?", sender_conn.getblocking())

            # get messages from the connection
            while True:
                msg = sender_conn.recv(1024)
                print("RECV", msg)

                # if there are 0 bytes received
                # then the remote socket closed
                if len(msg) == 0:
                    print("Client closed. Cleaning ...")
                    sender_conn.close()
                    break

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        if sender_conn.fileno() > 0:
            print("Sender socket was still open. Closing ...")
            sender_conn.close()
        receiver.close()

    print("RECEIVER STOP")


if __name__ == '__main__':
    main()
