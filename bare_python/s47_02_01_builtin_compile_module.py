from ut import p, p_items

from types import ModuleType


CODE_TEXT = """
def do_something(x: int) -> int:
    a = x * 100
    a = a + x
    return a

def do_that(y: int) -> float:
    # z = do_something(y)
    z = 6
    return z - y % 10
"""


def main() -> None:

    p("compiling ...")
    obj = compile(CODE_TEXT, "bla_module", "exec")

    p("compiled object")
    print(obj)

    p("dir of compiled object")
    obj_props = [
        str(x) for x in dir(obj)
        if not str(x).startswith("__")
    ]
    p_items(obj_props, 10)

    p("co_code")
    print(obj.co_code)

    p("evaluate ...")
    obj_mod = ModuleType("bla_mod")
    # passing the globals dict is important
    # because it will be populated first with do_something and after that
    # the definition of do_that will look for the signature of do_something
    # in the globals dict
    eval(obj, obj_mod.__dict__)
    print(dir(obj_mod))

    p("call do_something from obj_mod")
    print(
        "11 -> do_something -> ",
        str(obj_mod.do_that(11))
    )
    p("DONE")


if __name__ == '__main__':
    main()
