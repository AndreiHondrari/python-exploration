"""
Simple sender.
Just sends numbers to receiver.
"""

import time
import random
import socket


def main() -> None:
    print("SENDER START")
    sender = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "127.0.0.1"
    PORT = 5678
    sender.connect((HOST, PORT,))
    print("blocking sender?", sender.getblocking())

    try:
        while True:
            msg = f"{random.randint(1000, 10_000)}"
            print(f"SEND {msg}")
            sender.send(msg.encode())
            time.sleep(random.random() * 0.2)
    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        print("Cleaning ...")
        sender.close()

    print("SENDER STOP")


if __name__ == '__main__':
    main()
