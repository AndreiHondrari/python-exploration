"""
Receiver - multiplec receiver and client sockets

Steps:
- register receiver socket for selector
- start selecting
- when select catches an event check if it originates from the
  receiver socket, and if it does, simply register the new client socket
  for the selector
- if the caught event is not from the receiver socket, then it surely must be
  from one of the client sockets registered in between

Features:
- can connect and read client sockets at the same time
- clients can connect/disconnect at any time
"""
import selectors
import socket
import time
from typing import Set, Tuple, List

HOST = "localhost"
PORT = 5678


def main() -> None:
    print("RECEIVER START")

    # declare the selector
    selector = selectors.DefaultSelector()

    # declare first receiver
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver.bind((HOST, PORT,))
    receiver.setblocking(False)

    selector.register(receiver, selectors.EVENT_READ)

    receiver.listen()

    connections: Set[socket.socket] = set()

    try:
        event_pair: List[Tuple[selectors.SelectorKey, int]]
        while True:
            event_pairs = selector.select()
            events_count: int = len(event_pairs)

            for i in range(events_count):

                event_key: selectors.SelectorKey = event_pairs[i][0]
                event_flag: int = event_pairs[i][1]

                if event_flag & selectors.EVENT_READ:
                    # handle new connections
                    if event_key.fileobj == receiver:
                        new_connection, addr = receiver.accept()
                        print("New connection", addr)

                        new_connection.setblocking(False)
                        connections.add(new_connection)
                        selector.register(
                            new_connection,
                            selectors.EVENT_READ,
                            data=addr
                        )

                    # handle reads
                    else:
                        addr = event_key.data
                        msg_encoded = event_key.fileobj.recv(1024)
                        msg = msg_encoded.decode()
                        if len(msg) == 0:
                            print(f"Disconnected {addr}")
                            selector.unregister(event_key.fileobj)
                            connections.remove(event_key.fileobj)
                        else:
                            print(f"RECV[{addr}] {msg}")

                else:
                    print("OH :( not covered")

            time.sleep(0.2)
    except KeyboardInterrupt:
        print(" \nCtrl+C detected!")
    finally:
        print("Warm shutdown ...")
        receiver.close()
        for c in connections:
            c.close()

    print("RECEIVER END")


if __name__ == "__main__":
    main()
