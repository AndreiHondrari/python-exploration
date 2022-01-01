

def main() -> None:
    some_list = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    print("list:    ", some_list)
    print("list size:", len(some_list))

    print("reassign range")
    some_list[3:5] = [111 * i for i in range(6)]

    print('new list:', some_list)
    print("list size:", len(some_list))


if __name__ == "__main__":
    main()
