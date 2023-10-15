"""
Scheduling tasks with create_task, adds the tasks to the even loop
queue and makes sure that they are interchangeable when pausing.

This way, both coroutines get to start.
"""
import asyncio


async def do_foo():
    print("DO FOO")
    await asyncio.sleep(1)
    print("DO FOO POST")
    return 111


async def do_bar():
    print("DO BAR")
    await asyncio.sleep(0.5)
    print("DO BAR POST")
    return 222


async def do_some():
    print("\nZZZ")
    x_promise = asyncio.create_task(do_foo())
    y_promise = asyncio.create_task(do_bar())

    print("\nAA")
    x = await x_promise

    print("\nBB")
    y = await y_promise

    print(f"\nFIN | X {x} Y {y}")


def main() -> None:
    asyncio.run(do_some())


if __name__ == "__main__":
    main()
