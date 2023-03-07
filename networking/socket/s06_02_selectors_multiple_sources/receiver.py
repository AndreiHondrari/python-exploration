"""
Receiver - multiplexes fixed number of multiple clients

Steps:
- waits for multiple (fixed number) clients to connect
- registers each client socket to selector
- starts multiplexing for the sockets
- handles read events off the sockets as they come

Features:
- must wait for all clients to connect beforehand
- can handle all of the client sockets
- can not connect to additional clients while reading from connected ones


"""

import socket
import selectors
import time

from typing import Tuple, Set, List

SEPARATOR = '-' * 20

NO_OF_CLIENTS = 3


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

    connections: Set[socket.socket] = set()

    try:
        # wait for a connection
        while True:
            print(SEPARATOR)
            print("--- new session  ---")
            print("wait for accept ...")
            sender_conn: socket.socket
            addr: Tuple[str, int]

            for i in range(NO_OF_CLIENTS):
                (sender_conn, addr,) = receiver.accept()
                print(f"accepted! ({addr})")

                connections.add(sender_conn)
                sender_conn.setblocking(False)

                print("register for select ...")
                default_selector.register(
                    sender_conn,
                    selectors.EVENT_READ,
                    addr
                )

            # get messages from the connection
            is_running = True
            while is_running:
                # --- IMPORTANT BIT ----

                print("Select ...")
                event_pairs: List[Tuple[selectors.SelectorKey, int]]
                event_pairs = default_selector.select()
                events_count = len(event_pairs)
                print("Events count", events_count)

                for i in range(events_count):
                    event_key = event_pairs[i][0]
                    event_flag = event_pairs[i][1]
                    addr = event_key.data

                    if event_flag & selectors.EVENT_READ:
                        print("Read event")

                        msg = event_key.fileobj.recv(1024)
                        print(f"RECV {addr}", msg)

                        # if there are 0 bytes received
                        # then the remote socket closed
                        if len(msg) == 0:
                            print(f"Client {addr} closed. Cleaning ...")
                            default_selector.unregister(event_key.fileobj)
                            event_key.fileobj.close()
                            connections.remove(event_key.fileobj)

                print(SEPARATOR)
                print("LENCO", len(connections))
                if len(connections) == 0:
                    is_running = False

                time.sleep(0.5)  # artificial delay

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    finally:
        print("Cleaning ...")
        for sender_conn in connections:
            if sender_conn.fileno() > 0:
                print("Sender socket was still open. Closing ...")
                default_selector.unregister(sender_conn)
                sender_conn.close()

        receiver.close()

    print("RECEIVER STOP")


if __name__ == '__main__':
    main()
