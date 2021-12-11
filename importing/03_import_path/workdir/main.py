import sys
import site
import pathlib


def main() -> None:
    print("Importing unexisting")
    try:
        import mod1
    except ImportError as ierr:
        print("ERR CAUGHT", repr(ierr), "\n")

    print("Importing outside module")
    sys.path.append("../outside_dir")
    import mod1
    mod1.do_play_jazz()

    print("\nImport from alternative site packages")
    alt_site_packages = pathlib.Path("../alternative_site_packages_dir")
    site.addsitedir(str(alt_site_packages.absolute()))
    import mod2
    mod2.do_the_shaky()


if __name__ == '__main__':
    main()
