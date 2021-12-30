import time


def main():

    try:
        while True:
            print(".", end="", flush=True)
            time.sleep(1)
    except InterruptedError as ierr:
        print("INTR", repr(ierr))

    print("\nTERMINATED")


if __name__ == '__main__':
    main()
