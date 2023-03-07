"""
Receiver

Steps:
- Waits for a connection
- Registers a selector for the remote socket after accept
- Waits for messages from the remote socket

Features:
- Will not handle any other clients until current one finishes
"""

import socket
import selectors
import time

from typing import Tuple, List


def main() -> None:
    print("RECEIVER START")

    default_selector = selectors.DefaultSelector()

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

            sender_conn.setblocking(False)

            print("register for select ...")
            default_selector.register(sender_conn, selectors.EVENT_READ)

            # get messages from the connection
            is_running = True
            while is_running:
                # --- IMPORTANT BIT ----

                print("Select ...")
                event_pairs: List[Tuple[selectors.SelectorKey, int]]
                event_pairs = default_selector.select()
                print("Events count", len(event_pairs))
                for i in range(len(event_pairs)):
                    if event_pairs[i][1] & selectors.EVENT_READ:
                        print("Read event")

                        msg = sender_conn.recv(1024)
                        print("RECV", msg)

                        # if there are 0 bytes received
                        # then the remote socket closed
                        if len(msg) == 0:
                            print("Client closed. Cleaning ...")
                            default_selector.unregister(sender_conn)
                            sender_conn.close()
                            is_running = False
                            break

                time.sleep(0.5)  # artificial delay

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        if sender_conn.fileno() > 0:
            print("Sender socket was still open. Closing ...")
            default_selector.unregister(sender_conn)
            sender_conn.close()
        receiver.close()

    print("RECEIVER STOP")


if __name__ == '__main__':
    main()
