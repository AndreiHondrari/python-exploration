import random
import asyncio


async def do_something() -> int:
    print("Doing something time consuming ... (wait)")
    await asyncio.sleep(2)
    return random.randint(0, 100)


async def do_something_else() -> int:
    print("Doing something >ELSE< time consuming ... (wait)")
    await asyncio.sleep(1)
    return random.randint(100, 1000)


async def main() -> None:
    promise = do_something()
    promise2 = do_something_else()

    first_result = await promise
    second_result = await promise2

    print(f"Result 1st: {first_result} 2nd: {second_result}")


if __name__ == "__main__":
    main_promise = main()
    asyncio.run(main_promise)
