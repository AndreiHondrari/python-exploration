import socket


def main() -> None:
    print("\nRECEIVER START")
    receiver = socket.socket(
        socket.AF_INET,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    HOST = "0.0.0.0"
    PORT = 5678

    # nothing else is neccessary (like listen or accept)
    receiver.bind((HOST, PORT,))

    # compared to TCP, UDP uses the receiver socket to receive
    msg = receiver.recv(1024)

    print("RECV", msg)

    receiver.close()
    print("RECEIVER END")


if __name__ == '__main__':
    main()
