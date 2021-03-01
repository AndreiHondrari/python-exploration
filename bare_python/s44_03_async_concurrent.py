import random
import asyncio


async def do_something() -> int:
    print("Doing something time consuming ... (wait)")
    await asyncio.sleep(2)
    print("do_something finished time constuming thing")
    return random.randint(0, 100)


async def do_something_else() -> int:
    print("Doing something >ELSE< time consuming ... (wait)")
    await asyncio.sleep(1)
    print("do_something_else finished time constuming thing")
    return random.randint(100, 1000)


async def main() -> None:
    promise = do_something()
    promise2 = do_something_else()

    results = await asyncio.gather(
        promise,
        promise2,
    )

    print(f"Result {results}")


if __name__ == "__main__":
    main_promise = main()
    asyncio.run(main_promise)
