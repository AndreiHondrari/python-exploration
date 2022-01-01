

def main() -> None:
    LIMIT = 20
    list_one = [x for x in range(LIMIT) if x % 2 == 0]  # even
    list_two = [x for x in range(LIMIT) if (x+1) % 2 == 0]  # odd

    print("LIST ONE:", list_one)
    print("LIST TWO:", list_two)

    some_slice = slice(3, 6)

    print("SLICE ONE", list_one[some_slice])
    print("SLICE TWO", list_two[some_slice])


if __name__ == "__main__":
    main()
