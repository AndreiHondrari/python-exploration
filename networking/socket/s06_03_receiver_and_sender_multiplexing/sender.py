"""
Simple sender.
Just sends numbers to receiver.
"""

import socket
import time
import random

HOST = "localhost"
PORT = 5678


def main() -> None:
    print("SENDER START")

    sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender.connect((HOST, PORT,))

    try:
        while True:
            msg = f"{random.randint(1000, 10_000)}"
            print(f"SEND {msg}")
            sender.send(msg.encode())
            time.sleep(random.random() * 0.5 + 0.2)
    except KeyboardInterrupt:
        print(" \nCtrl+C detected!")
    finally:
        print("Warm shutdown ...")
        sender.close()

    print("SENDER END")


if __name__ == "__main__":
    main()
