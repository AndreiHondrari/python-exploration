import sub1


def main() -> None:
    try:
        sub1.mod1.do_something()
    except AttributeError:
        print("IMPORT ERROR")

    print("DIR:", dir(sub1))
    print(type(sub1))


if __name__ == '__main__':
    main()
