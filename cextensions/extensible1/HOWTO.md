# Guide for compiling a .c file into a shared library (.so)

Steps for creating a cpython extension can be [seen here](http://book.pythontips.com/en/latest/python_c_extension.html)

## Command to compile
> gcc -shared -Wl,-soname,someext -o someext.so -fPIC someext.c

## Options
- `-shared`: marks the compilation to a `.so` shared lib file
- `-Wl`: comma separated options for the linker. `-soname` specified for the linker the extension name explained in [greater detail here](https://stackoverflow.com/a/14613602/858565)
- `-o`: output file name
- `-fPIC`: special option passed to subprocesses of GCC. The official definition for this option is:
> emit position-independent code, suitable for dynamic linking and avoiding any limit on the size of the global offset table
