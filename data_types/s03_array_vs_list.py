import array
import functools
import sys
import time
import random
from decimal import Decimal as D
from typing import Iterable, Tuple

hprint = functools.partial(print, "\n#")
give_int = functools.partial(random.randint, 0, 10_000)


def get_bytes_size(iterable: Iterable[int]) -> Tuple[D, int]:
    bytes_size = D(float(sys.getsizeof(iterable)))

    order = 0
    while True:
        new_size = bytes_size / D(1024.0)

        if int(new_size) == 0:
            break

        order += 1
        bytes_size = new_size

    return round(bytes_size, 2), order


BYTES_ORDER = {
    0: '',
    1: 'K',
    2: 'M',
    3: 'G',
    4: 'T',
}


def print_i_every(i: int, ref: int) -> None:
    if i % ref == 0:
        print("\r", " " * 10, "\r", sep='', end='', flush=True)
        i_str = f"{i:,}".replace(",", " ")
        print(i_str, end='', flush=True)


def main() -> None:
    SIZE = 100_000_000
    MID = SIZE // 2

    SIZE_STR = f"{SIZE:,}".replace(',', ' ')
    hprint(f"define the array ({SIZE_STR} elements)", flush=True)
    some_array = array.array('Q')  # unsigned long long

    hprint("populate array", flush=True)
    VERY_LARGE_NUMBER = int.from_bytes((b'\xff' * 8), 'big')
    for i in range(SIZE):
        print_i_every(i, 100_000)
        some_array.append(VERY_LARGE_NUMBER)
    print("\n")

    size, order = get_bytes_size(some_array)
    print(
        "array of size:",
        size, BYTES_ORDER.get(order, "MANY"), "bytes",
        flush=True
    )

    hprint("export array to list")
    some_list = some_array.tolist()
    size, order = get_bytes_size(some_list)
    print(
        "list of size:",
        size, BYTES_ORDER.get(order, "MANY"), "bytes",
        flush=True
    )

    new_number = give_int()

    # ---
    hprint("insert into array at end", flush=True)
    start = time.time()
    some_array.append(new_number)
    stop = time.time()
    time_delta = round(stop - start, 10)
    print(f"time spent: {time_delta:f} seconds", flush=True)

    # ---
    hprint("insert into list at end", flush=True)
    start = time.time()
    some_list.append(new_number)
    stop = time.time()
    time_delta = round(stop - start, 10)
    print(f"time spent: {time_delta:f} seconds")

    # ---
    hprint("insert into array in middle")
    start = time.time()
    some_array.insert(MID, new_number)
    stop = time.time()
    time_delta = round(stop - start, 10)
    print(f"time spent: {time_delta:f} seconds", flush=True)

    # ---
    hprint("insert into list in middle", flush=True)
    start = time.time()
    some_list.insert(MID, new_number)
    stop = time.time()
    time_delta = round(stop - start, 10)
    print(f"time spent: {time_delta:f} seconds", flush=True)


if __name__ == "__main__":
    main()
