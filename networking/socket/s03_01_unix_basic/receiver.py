"""
NOTICE THAT COMPARED WITH THE OTHER EXAMPLES
IN THIS EXAMPLE THE FAMILY CHANGES INSTEAD OF THE SOCKET TYPE
"""

import os
import pathlib
import socket


def main() -> None:
    print("\nRECEIVER START")
    receiver = socket.socket(
        socket.AF_UNIX,  # socket family
        socket.SOCK_DGRAM,  # socket type
    )

    SOCKET_FILE = "gandalf.sock"
    socket_file_path = pathlib.Path(f"./{SOCKET_FILE}").absolute()
    if socket_file_path.exists():
        print(f"Socket {str(socket_file_path)} already exists. Removing ...")
        os.remove(str(socket_file_path))
    receiver.bind(SOCKET_FILE)

    print("wait for recv ...")
    msg = receiver.recv(1024)

    print("RECV", msg)

    receiver.close()
    print("RECEIVER END")


if __name__ == '__main__':
    main()
