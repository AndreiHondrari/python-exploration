import sys
import functools
import pathlib
import importlib as ilib
from importlib import resources as ilib_resources

from types import ModuleType

hprint = functools.partial(print, "\n#")


class PluginResourceReader(ilib.abc.ResourceReader):
    pass


def f1() -> None:
    print("DO KEK")


class PluginLoader(ilib.machinery.SourceFileLoader):

    def exec_module(self, module: ModuleType) -> None:
        # super().exec_module(module)

        print("EXEC_MODULE", module)
        if hasattr(module, 'install'):
            module.install()

    def get_resource_reader(self, fullname: str) -> PluginResourceReader:
        print("GET_RESOURCE_READER", fullname)
        return PluginResourceReader()


class MyPluginFinder(ilib.abc.MetaPathFinder):

    def find_spec(
        plugin_name: str,
        path: pathlib.PurePath,
        target
    ) -> ilib.machinery.ModuleSpec:

        print("FIND_SPEC_FULLNAME", plugin_name)
        print("FIND_SPEC_PATH", path)
        print("FIND_SPEC_TARGET", target)

        if not plugin_name.startswith('plugin_'):
            raise ModuleNotFoundError

        normal_name = plugin_name.replace("plugin_", "")
        print("FIND_SPEC_NORMAL_NAME", normal_name)

        plugin_path = pathlib.Path("plugins").absolute().joinpath(normal_name)
        print("FIND_SPEC_PLUGIN_PATH", plugin_path)

        fullname = f"plugins.{normal_name}"
        plugin_loader = PluginLoader(fullname, plugin_path)

        spec = ilib.machinery.ModuleSpec(
            name=fullname,
            loader=plugin_loader,
            origin=str(plugin_path),
            is_package=True,
            # parent=fullname,
            # has_location=True,
        )

        spec.has_location = True
        spec.submodule_search_locations = [str(plugin_path)]
        # import ipdb; ipdb.set_trace()
        return spec


def main() -> None:
    hprint("Import pack1")
    sys.meta_path.append(MyPluginFinder)
    import plugin_pack1
    ilib.import_module

    hprint("Show pack1 member")
    for x in dir(plugin_pack1):
        if not x.startswith('_'):
            print(x)

    hprint("Use pack1")
    # import ipdb; ipdb.set_trace()
    plugin_pack1.mod1.do_something()

    hprint("Use pack1 resources")
    print("SUBMOD SL:", plugin_pack1.__spec__.submodule_search_locations)
    resource_container = ilib_resources.files(plugin_pack1)
    print(resource_container)


if __name__ == "__main__":
    main()
