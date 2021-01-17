import time


async def do_something():
    time.sleep(1)
    print("Do something")


if __name__ == "__main__":
    promise = do_something()
    await promise
