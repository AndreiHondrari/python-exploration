import time
import socket
import random


def main() -> None:
    print("START CLIENT")

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_sock.connect(("127.0.0.1", 5555,))

        while True:
            val = random.randint(100, 1_000)
            print("SND", val)
            server_sock.sendall(str(val).encode())
            time.sleep(0.25)

    except KeyboardInterrupt:
        print("\nCtrl+C")

    server_sock.close()

    print("STOP CLIENT")


if __name__ == "__main__":
    main()
