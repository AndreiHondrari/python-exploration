import importlib as ilib
import functools

from types import ModuleType
from typing import Optional

hprint = functools.partial(print, "\n#")


def main() -> None:
    path_finder = ilib.machinery.PathFinder()

    hprint("mod1 spec")
    mod1_spec = path_finder.find_spec('mod1')
    print(type(mod1_spec))

    for x in dir(mod1_spec):
        if not x.startswith('_'):
            print(f"mod1_spec.{x} ->", getattr(mod1_spec, x))

    hprint("Load")
    mod1: Optional[ModuleType] = None
    if isinstance(mod1_spec.loader, ilib.machinery.SourceFileLoader):
        # THIS IS DEPRECATED
        # mod1_spec.loader.load_module(mod1_spec.name)

        mod1 = mod1_spec.loader.create_module(mod1_spec)

        # if create_module didn't work
        if mod1 is None:
            mod1 = ModuleType(name=mod1_spec.name)

            mod1.__loader__ = mod1_spec.loader
            mod1.__package__ = mod1_spec.parent
            mod1.__spec__ = mod1_spec
            # mod1.__path__  # this is reserved for packages
            mod1.__file__ = mod1_spec.origin
            mod1.__cached__ = mod1_spec.cached

        mod1_spec.loader.exec_module(mod1)
        print(mod1)
    else:
        print("NOT A SOURCE FILE LOADER !")

    hprint("Use")
    if mod1 is None:
        print("mod1 WAS NOT LOADED !")
    else:
        mod1.do_something()


if __name__ == "__main__":
    main()
