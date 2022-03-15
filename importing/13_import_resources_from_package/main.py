import importlib as ilib
from importlib import resources as ilib_resources
import functools

import pack1

hprint = functools.partial(print, "\n#")


def main() -> None:
    hprint("The resource container")
    pack1_resource_container = ilib_resources.files(pack1)
    print(
        "pack1 resource container:",
        pack1_resource_container
    )

    hprint("Contents")
    contents = ilib_resources.contents(pack1)
    for c in contents:
        print(c)

    hprint("As file")
    pack1_rc_file_context_manager = ilib_resources.as_file(
        pack1_resource_container
    )

    with pack1_rc_file_context_manager as posix_file:
        print(type(posix_file), posix_file)

    hprint("Open text")
    hello_stream = ilib_resources.open_text(pack1, "hello.txt")
    hello_line = hello_stream.readline()
    print(hello_line, end="")

    hprint("Resource path")
    resource_path = ilib_resources.path(pack1, "hello.txt")
    print(resource_path)


if __name__ == "__main__":
    main()
