from typing import List
from dataclasses import dataclass


class BlaIterator:

    def __init__(self, bla: 'Bla') -> None:
        self.bla = bla
        self.i = 0
        self.j = 0

    def __next__(self) -> int:

        if self.i < len(self.bla.kek):
            value = self.bla.kek[self.i]
            self.i += 1
            return value

        if self.j < len(self.bla.lol):
            value = self.bla.lol[self.j]
            self.j += 1
            return value

        raise StopIteration


@dataclass
class Bla:
    kek: List[int]
    lol: List[int]

    def __iter__(self) -> BlaIterator:
        return BlaIterator(self)


def main() -> None:
    b1 = Bla(kek=[11, 22, 33, 44], lol=[55, 66, 77, 88, 99])

    for k in b1:
        print(k)


if __name__ == "__main__":
    main()
