try:
    from root.sub1.mod1 import do_that
except ImportError:
    print("Can't import sub1.mod1 because of mod2 import problems")

    def do_that() -> None:
        pass


def main() -> None:
    print(f"MF {__file__}")
    print(f"MN {__name__}")
    print(f"MP {__package__}", end="\n\n")
    do_that()


if __name__ == '__main__':
    main()
