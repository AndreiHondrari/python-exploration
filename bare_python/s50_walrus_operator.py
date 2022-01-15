
from typing import Optional, Callable

k = 0


def get_number_producer_func(max_value: int) -> Callable[[], Optional[int]]:
    def _func() -> Optional[int]:
        global k
        if k >= max_value:
            return None

        k += 1
        return k

    return _func


def main() -> None:

    give_number = get_number_producer_func(2)

    while (number := give_number()) is not None:
        print(number)


if __name__ == "__main__":
    main()
