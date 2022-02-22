import random
import functools

from typing import List, Union, Tuple, cast

hprint = functools.partial(print, "\n#")


class Matrix:

    @property
    def rows_count(self) -> int:
        return self._rows_count

    @property
    def cols_count(self) -> int:
        return self._cols_count

    def __init__(
        self,
        rows_count: int,
        cols_count: int
    ) -> None:
        self._rows_count = rows_count
        self._cols_count = cols_count

        self._matrix: List[List[int]] = [
            [0 for j in range(cols_count)]
            for i in range(rows_count)
        ]

    def __getitem__(
        self,
        limits: Tuple[Union[int, slice], Union[int, slice]]
    ) -> Union[int, List[int], List[List[int]]]:
        assert isinstance(limits, tuple)
        assert len(limits) == 2

        rows_limits = limits[0]
        cols_limits = limits[1]

        if isinstance(rows_limits, int) and rows_limits >= self._rows_count:
            raise IndexError("Out of rows range")

        if isinstance(cols_limits, int) and cols_limits >= self._cols_count:
            raise IndexError("Out of cols range")

        if isinstance(rows_limits, int):
            cols = self._matrix[rows_limits]
            return cols[cols_limits]

        elif isinstance(rows_limits, slice):
            rows = self._matrix[rows_limits]
            return cast(
                Union[int, List[int], List[List[int]]],
                list(map(lambda row: row[cols_limits], rows))
            )

    def __setitem__(
        self,
        limits: Tuple[int, int],
        value: int
    ) -> None:
        assert isinstance(limits, tuple)
        assert len(limits) == 2

        self._matrix[limits[0]][limits[1]] = value


def main() -> None:
    m1 = Matrix(3, 5)

    hprint("Initialized a matrix")
    for i in range(m1.rows_count):
        for j in range(m1.cols_count):
            m1[i, j] = random.randint(100, 999)

    hprint("Display matrix by singular indices")
    for i in range(m1.rows_count):
        for j in range(m1.cols_count):
            x = m1[i, j]
            print(f"{x: >3}", end=" ")

        print()

    hprint("Display matrix by slicing rows")
    print(m1[:2, 0])

    hprint("Display matrix by slicing cols")
    print(m1[0, :3])

    hprint("Display matrix by slicing both rows and cols")
    print(m1[1:, 2:4])


if __name__ == "__main__":
    main()
