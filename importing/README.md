# Import system

## The import mechanism

## Packages

### Namespace packages

These are simply directories that do not have an `__init__.py` module in them.

To import from these you have to specify exact names.

Assuming we have the following tree structure:

```yaml
- root
  - mynamespace
    - module1.py
    - package1
      - __init__.py
      - submodule1.py
```

Then we can do these:

```python
from mynamespace import module1
```

```python
from mynamespace import package1

package1.submodule1.do_this()
```

But we can not do these:

```python
import mynamespace

mynamespace.mod1.do_something()
```
