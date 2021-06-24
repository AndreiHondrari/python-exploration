

from ut import p


class BaseClassGamma:

    x = 1

    @classmethod
    def change(cls) -> None:
        cls.x *= 2


class BaseClassDelta:

    y = 1

    @classmethod
    def change(cls) -> None:
        BaseClassDelta.y *= 2


class SubclassJeff(BaseClassGamma):
    pass


class SubclassXavier(BaseClassDelta):
    pass


if __name__ == '__main__':

    p("Test BaseClassGamma")
    print(f"Initial BaseClassGamma.x: {BaseClassGamma.x}")
    print(f"Initial SubclassJeff.x: {SubclassJeff.x}")

    # When changing from superclass, also subclass class variables
    # are affected
    p("Changing from BaseClassGamma")
    BaseClassGamma.change()
    print(f"BaseClassGamma.x: {BaseClassGamma.x}")
    print(f"SubclassJeff.x: {SubclassJeff.x}")

    # When changing from subclass, ONLY subclass class variables
    # are affected
    p("Changing from SubclassJeff")
    SubclassJeff.change()
    print(f"BaseClassGamma.x: {BaseClassGamma.x}")
    print(f"SubclassJeff.x: {SubclassJeff.x}")

    # Subsequent changing from base class will override previous subclass
    # static variable state
    p("Changing again from BaseClassGamma")
    BaseClassGamma.change()
    print(f"BaseClassGamma.x: {BaseClassGamma.x}")
    print(f"SubclassJeff.x: {SubclassJeff.x}")

    p("Test BaseClassDelta")
    print(f"Initial BaseClassDelta.y: {BaseClassDelta.y}")
    print(f"Initial SubclassXavier.y: {SubclassXavier.y}")

    # When using the superclass name directly in the class methods
    # instead of passed cls argument, there is only one state that changes
    # throughout the whole inheritance tree
    p("Changing from BaseClassDelta")
    BaseClassDelta.change()
    print(f"BaseClassDelta.y: {BaseClassDelta.y}")
    print(f"SubclassXavier.y: {SubclassXavier.y}")

    p("Changing from SubclassXavier")
    SubclassXavier.change()
    print(f"BaseClassDelta.y: {BaseClassDelta.y}")
    print(f"SubclassXavier.y: {SubclassXavier.y}")

    p("Changing again from BaseClassDelta")
    BaseClassDelta.change()
    print(f"BaseClassDelta.y: {BaseClassDelta.y}")
    print(f"SubclassXavier.y: {SubclassXavier.y}")
