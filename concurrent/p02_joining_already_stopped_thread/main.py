import random
import time
import threading


def bla():
    print("thread started")
    print("thread done")


def main() -> None:
    print("START")
    thread = threading.Thread(target=bla)

    print("starting thread from main")
    thread.start()

    print("sleeping")
    time.sleep(2)
    print("sleep done")

    print("join thread")
    thread.join()
    print("join passed")

    print("END")


if __name__ == '__main__':
    main()
