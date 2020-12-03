#!python
import copy
from decimal import Decimal, getcontext, setcontext

from ut import p

initial_context = getcontext()

# with initial context
p("0.1 + 0.2 plain floats")
print(0.1 + 0.2)

p("Decimal('0.1') + Decimal('0.2') --> from strings")
print(Decimal('0.1') + Decimal('0.2') )

p(f"Decimal(0.1) + Decimal(0.2) --> from floats with precision: {initial_context.prec}")
print(Decimal(0.1) + Decimal(0.2) )

p(f"Decimal((0, (1,), -1)) + Decimal((0, (2,), -1))")
print(Decimal((0, (1,), -1)) + Decimal((0, (2,), -1)))

# with altered context
altered_context = copy.deepcopy(initial_context)
altered_context.prec = 2
p(f"set new context with precision: {altered_context.prec}")
setcontext(altered_context)

p(f"alter context with precision: {altered_context.prec}")

p(f"Decimal(0.1) + Decimal(0.2) --> from floats with precision: {initial_context.prec}")
print(Decimal(0.1) + Decimal(0.2) )