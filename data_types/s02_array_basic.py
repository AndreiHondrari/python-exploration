import array
import functools

hprint = functools.partial(print, "\n#")


def main() -> None:
    some_array = array.array('i')

    some_array.append(11)
    some_array.append(22)

    hprint("Trying to append a different type")
    try:
        some_array.append("abc")  # type: ignore[arg-type]
    except TypeError as terr:
        print("Caught", repr(terr))

    hprint("Our array")
    print(some_array)


if __name__ == "__main__":
    main()
