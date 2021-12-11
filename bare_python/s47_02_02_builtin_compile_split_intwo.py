from ut import p, p_items

from types import ModuleType


CODE_TEXT_PART_1 = """
def do_something(x: int) -> int:
    a = x * 100
    a = a + x
    return a
"""

CODE_TEXT_PART_2 = """
def do_that(y: int) -> float:
    # z = do_something(y)
    z = 6
    return z - y % 10
"""


def main() -> None:

    # ---
    # FIRST COMPILATION
    # ---
    p("compiling ...")
    obj = compile(CODE_TEXT_PART_1, "bla_module", "exec")

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
    eval(obj, obj_mod.__dict__)
    print(dir(obj_mod))

    p("call do_something from obj_mod")
    print(
        "11 -> do_something -> ",
        str(obj_mod.do_something(11))
    )

    # ---
    # SECOND COMPILATION
    # ---
    p("try to use do_something in a different compile")
    obj_2 = compile(CODE_TEXT_PART_2, "bla_module_2", "exec")
    obj_mod_2 = ModuleType("bla_mod_2")
    eval(
        obj_2,
        obj_mod_2.__dict__
    )
    print(dir(obj_mod_2))

    p("use do_that")
    print(
        "11 -> do_that -> ",
        str(obj_mod_2.do_that(22))
    )

    p("DONE")


if __name__ == '__main__':
    main()
