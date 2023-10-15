"""
Notice that calling multiple awaits one after another
does not mean the event loop will pick them up as concurrent tasks.
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
    p1 = do_foo()
    p2 = do_bar()

    print("\nAA")
    x = await p1

    print("\nBB")
    y = await p2

    print(f"\nFIN | X {x} Y {y}")


def main() -> None:
    asyncio.run(do_some())


if __name__ == "__main__":
    main()
