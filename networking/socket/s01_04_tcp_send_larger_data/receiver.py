import time
import socket


def main() -> None:
    print("START RECEIVER")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = ""
    PORT = 5678
    receiver.bind((HOST, PORT,))

    print("Listen ...")
    receiver.listen()

    sender_conn: socket.socket

    try:
        while True:
            print("Wait to accept ...")
            (sender_conn, addr, ) = receiver.accept()
            print(f"Accepted {addr}")

            print("Receive ...")
            while True:
                msg = sender_conn.recv(1024)
                print("RECV", msg[:10], " ...", str(len(msg)))

                if len(msg) == 0:
                    print("Remote closed. Cleaning ...")
                    sender_conn.close()
                    break

                time.sleep(0.01)  # simulate slow recv

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        if sender_conn.fileno() > 0:
            sender_conn.close()

        receiver.close()

    print("END RECEIVER")


if __name__ == '__main__':
    main()
