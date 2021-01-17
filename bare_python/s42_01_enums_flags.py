#!python3

import enum

from ut import p

p("Explore flags")


class IOMode(enum.Flag):
    READ = 0b0001
    WRITE = 0b0010
    APPEND = 0b0100
    BINARY = 0b1000


p("IOMode.READ | IOMode.WRITE")
mode = IOMode.READ | IOMode.WRITE
print(f"mode: {mode}")
print(f"hex(mode.value): {hex(mode.value)}")


def openfile(filename: str, mode: IOMode) -> None:
    p(f"Opening file {filename} ...")

    if mode & IOMode.READ:
        print(f"Opening READ stream for {filename}")

    if mode & IOMode.WRITE and mode & IOMode.APPEND:
        raise Exception(
            "I/O Exception. Can't open a file in APPEND and WRITE "
            "at the same time"
        )

    if mode & IOMode.WRITE:
        print(f"Opening WRITE stream for {filename}")

    if mode & IOMode.APPEND:
        print(f"Opening APPEND stream for {filename}")

    if mode & IOMode.BINARY:
        print(f"Set BINARY mode for {filename}")


openfile("file1", IOMode.READ)
openfile("file2", IOMode.READ | IOMode.WRITE)
openfile("file3", IOMode.READ | IOMode.WRITE | IOMode.BINARY)
openfile("file4", IOMode.APPEND | IOMode.BINARY)

try:
    openfile("file5", IOMode.WRITE | IOMode.APPEND)
except Exception as e:
    print(f"raised: {e}")
