from typing import Any, List


def p(m: Any) -> None:
    print("\n###", str(m))  # noqa


def p_items(
    items: List[str],
    per_row: int = 5
) -> None:

    out_list: List[str] = []
    items_iter = iter(items)

    try:
        while True:
            out_list = []
            for i in range(per_row):
                out_list.append(next(items_iter))

            print(", ".join(out_list))

    except StopIteration:
        print(", ".join(out_list))
