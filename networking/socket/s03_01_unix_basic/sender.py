"""
NOTICE THAT COMPARED WITH THE OTHER EXAMPLES
IN THIS EXAMPLE THE FAMILY CHANGES INSTEAD OF THE SOCKET TYPE
"""

import socket


def main() -> None:
    print("\nSENDER START")
    sender = socket.socket(
        socket.AF_UNIX,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    SOCKET_FILE = "gandalf.sock"

    sender.connect(SOCKET_FILE)

    print("sending ...")
    sender.send(b"hello other node!")

    print("SENDER END")


if __name__ == '__main__':
    main()
