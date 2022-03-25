import socketserver


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        while True:
            msg = self.request.recv(1024)
            if msg == b'':
                print("REMOTE CLOSED")
                return

            print(msg)


def main() -> None:
    print("START SERVER")

    tcp_server = socketserver.TCPServer(
        ("127.0.0.1", 5555),
        TCPHandler,
        bind_and_activate=False
    )

    try:
        tcp_server.server_bind()
        tcp_server.server_activate()
        tcp_server.serve_forever()

    except KeyboardInterrupt:
        print("\nCtrl+C")

    finally:
        tcp_server.server_close()

    print("STOP SERVER")


if __name__ == "__main__":
    main()
