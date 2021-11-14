import time
import random
from threading import Thread, Event


def do_some(stop_event: Event):
    UID = random.randint(1000, 10_000)
    print(f"RUNNER [{UID}] STARTED")
    while not stop_event.is_set():
        print(f"[{UID}] hey")
        time.sleep(1)


def main():
    stop_event = Event()
    t1 = Thread(target=do_some, args=(stop_event,))
    t2 = Thread(target=do_some, args=(stop_event,))

    t1.start()
    t2.start()

    try:
        t1.join()
        t2.join()
    except (KeyboardInterrupt, SystemExit,):
        print("\nStop detected")
        stop_event.set()
        t1.join()
        t2.join()
        print("Terminated")


if __name__ == '__main__':
    print("Execution started")
    main()
    print("Finish")
