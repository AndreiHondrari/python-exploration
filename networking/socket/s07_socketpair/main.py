import time
import math
import random
import socket
import threading
import select


def do_recv(
    stop_event: threading.Event,
    receiver_socket: socket.socket
) -> None:
    SELECT_TIMEOUT = 0.1

    while not stop_event.is_set():
        to_read, _, to_err = select.select(
            [receiver_socket], [], [receiver_socket], SELECT_TIMEOUT
        )
        if len(to_read) > 0:
            msg = receiver_socket.recv(1024)
            print(f"[RECVER] RCV {msg!r}", flush=True)


def do_send(
    stop_event: threading.Event,
    sender_socket: socket.socket
) -> None:
    while not stop_event.is_set():
        value = random.randint(1000, 10_000)
        msg = value.to_bytes(
            math.ceil(value.bit_length() / 8),
            'big'
        )
        print(f"[SENDER] SND {msg!r}", flush=True)
        sender_socket.send(msg)
        time.sleep(random.random())


def main() -> None:
    print("[MAIN] START")

    print("[MAIN] create sockets ...")
    receiver_socket, sender_socket = socket.socketpair(
        socket.AF_UNIX, socket.SOCK_DGRAM
    )

    print("[MAIN] starting threads ...")
    stop_event = threading.Event()

    receiver_thread = threading.Thread(
        target=do_recv,
        args=(stop_event, receiver_socket,)
    )
    receiver_thread.daemon = True

    sender_thread = threading.Thread(
        target=do_send,
        args=(stop_event, sender_socket,)
    )
    sender_thread.daemon = True

    receiver_thread.start()
    sender_thread.start()

    print("[MAIN] running threads ...")
    try:
        receiver_thread.join()
        sender_thread.join()
    except KeyboardInterrupt:
        print("\nCtrl+C detected!")
    finally:
        print("Shutting down ...")
        stop_event.set()

        print("Wait for threads to finish ...")
        receiver_thread.join(timeout=5)
        sender_thread.join(timeout=5)

        print("[MAIN] Cleaning sockets ...")
        sender_socket.close()
        receiver_socket.close()

    print("[MAIN] STOP")


if __name__ == '__main__':
    main()
