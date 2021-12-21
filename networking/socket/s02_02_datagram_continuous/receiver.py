import socket


def main() -> None:
    print("\nRECEIVER START")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678

    receiver.bind((HOST, PORT,))

    print("waiting ...")
    try:
        while True:
            msg = receiver.recv(1024)
            print("RECV", msg)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    receiver.close()
    print("RECEIVER END")


if __name__ == '__main__':
    main()
