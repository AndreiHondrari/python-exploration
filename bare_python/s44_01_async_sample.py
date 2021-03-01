import random
import asyncio


async def do_something() -> int:
    print("Doing something time consuming ... (wait)")
    await asyncio.sleep(2)
    return random.randint(0, 100)


if __name__ == "__main__":
    promise = do_something()
    result = asyncio.run(promise)
    print(f"Result {result}")
