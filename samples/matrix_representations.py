
import functools
import random

hprint = functools.partial(print, "\n#")


def main() -> None:
    ROWS = 3
    COLS = 5

    hprint("Matrix as list of lists")
    matrix1 = [
        [random.randint(0, 999) for j in range(COLS)]
        for i in range(ROWS)
    ]

    for i in range(ROWS):
        for j in range(COLS):
            cell_value = matrix1[i][j]
            print(f"{cell_value: >3}", end=" ")
        print()

    hprint("Matrix as dictionary of tuples -> values")
    matrix2 = {}

    for i in range(ROWS):
        for j in range(COLS):
            matrix2[i, j] = random.randint(0, 999)

    for i in range(ROWS):
        for j in range(COLS):
            cell_value = matrix1[i][j]
            print(f"{cell_value: >3}", end=" ")
        print()


if __name__ == "__main__":
    main()
