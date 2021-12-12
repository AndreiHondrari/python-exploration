import time
import socket
import errno


def main() -> None:
    print("START RECEIVER")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_STREAM,  # socket type
    )

    HOST = "0.0.0.0"
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

            print("Unblock sender")
            sender_conn.setblocking(False)

            print("Receive ...")
            while True:
                try:
                    msg = sender_conn.recv(1024)
                    print("RECV", msg)

                    if len(msg) == 0:
                        print("Remote closed. Cleaning ...")
                        sender_conn.close()
                        break

                except BlockingIOError as berr:
                    if berr.errno == errno.EAGAIN:
                        print("EAGAIN")
                    else:
                        print("Problem", errno.errorcode[berr.errno])

                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")
    finally:
        if sender_conn.fileno() > 0:
            sender_conn.close()

        receiver.close()

    print("END RECEIVER")


if __name__ == '__main__':
    main()
