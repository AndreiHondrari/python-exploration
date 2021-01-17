#!python3

import enum

from ut import p

p("Explore enums")


class Color(enum.Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4


p("get enum by value")

c1 = Color(3)
print(f"c1.name == 'GREEN': {c1.name == 'GREEN'}")
print(f"c1 == Color.GREEN: {c1 == Color.GREEN}")


def colorize(color: Color) -> None:
    print(f"colorized with: {color.name}")


p("colorize")
colorize(Color.RED)

p("color comparisons")
print(f"Color.RED == Color.BLUE {Color.RED == Color.BLUE}")
print(f"Color.RED == Color.RED {Color.RED == Color.RED}")

p("attempt Color.RED < Color.RED")
try:
    print(f"Color.RED < Color.RED {Color.RED < Color.RED}")  # type: ignore
except TypeError as e:
    print(f"raised: {e}")


p("attempt Color.RED + Color.RED")
try:
    print(f"Color.RED + Color.RED {Color.RED + Color.RED}")  # type: ignore
except TypeError as e:
    print(f"raised: {e}")

color_weights = {
    Color.RED: 100,
    Color.BLUE: 200
}

redweight = color_weights[Color.RED]
p("use Enum as key")
print(f"color_weights[Color.RED]: {redweight}")


class Constant(enum.IntEnum):
    CONST_1 = 10
    CONST_2 = 20


p("attempt Constant.CONST_1 < Constant.CONST_2")
try:
    const_cmp = Constant.CONST_1 < Constant.CONST_2
    print(f"Constant.CONST_1 < Constant.CONST_2 {const_cmp}")  # type: ignore
except TypeError as e:
    print(f"raised: {e}")


p("attempt Constant.CONST_1 + Constant.CONST_2")
try:
    const_sum = Constant.CONST_1 + Constant.CONST_2
    print(f"Constant.CONST_1 + Constant.CONST_2 {const_sum}")  # type: ignore
except TypeError as e:
    print(f"raised: {e}")
