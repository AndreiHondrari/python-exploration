import socket
import select

from typing import Tuple


def main() -> None:
    print("RECEIVER START")

    print("bind receiver ...")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678
    receiver.bind((HOST, PORT,))
    receiver.listen()

    try:
        # wait for a connection
        while True:
            print("wait for accept ...")
            sender_conn: socket.socket
            addr: Tuple[str, int]
            (sender_conn, addr,) = receiver.accept()
            print(f"accepted! ({addr})")

            # get messages from the connection
            while True:
                # --- IMPORTANT BIT ----
                print("Select ...")
                (
                    to_read, to_write, to_err
                ) = select.select([sender_conn], [], [sender_conn])

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
