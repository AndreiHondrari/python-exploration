import time
import socket
import errno


def main() -> None:
    print("\nRECEIVER START")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678

    receiver.bind((HOST, PORT,))

    print("unblock receiver")
    receiver.setblocking(False)

    print("waiting ...")
    try:
        while True:
            try:
                msg = receiver.recv(1024)
                print("RECV", msg)
            except BlockingIOError as berr:
                if berr.errno == errno.EAGAIN:
                    print("EAGAIN")
                else:
                    print("Problem", errno.errorcode[berr.errno])

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    receiver.close()
    print("RECEIVER END")


if __name__ == '__main__':
    main()
