
import socket
import logging
import struct
import pickle
from typing import Optional


def main() -> None:
    print("PARASITE_START")

    logging.basicConfig(level=1)
    root_logger = logging.getLogger()

    log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log_socket.bind(("127.0.0.1", 5678,))
    log_socket.listen()

    conn: Optional[socket.socket] = None

    try:
        while True:
            print('\n', '-' * 20, sep='')
            print(" -- NEW SESSION --")
            conn, addr = log_socket.accept()

            while True:
                # get the header
                header_size = struct.calcsize('>L')
                msg = conn.recv(header_size)

                if msg == b'':
                    print("\nREMOTE DIED")
                    break

                data_length = struct.unpack('>L', msg)[0]

                # get the log data
                total = 0
                body = b''

                while total < data_length:
                    diff = data_length - total
                    if diff < 1024:
                        chunk = conn.recv(diff)
                    else:
                        chunk = conn.recv(1024)

                    body += chunk
                    total = len(body)

                # deserialize the log record
                record_dict = pickle.loads(body)
                record = logging.makeLogRecord(record_dict)
                root_logger.handle(record)

    except KeyboardInterrupt:
        print("\nCtrl+C detected")

    if conn is not None:
        conn.close()

    log_socket.close()

    print("PARASITE_STOP")


if __name__ == "__main__":
    main()
