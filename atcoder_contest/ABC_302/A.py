import math
from decimal import Decimal

a, b = map(int, input().split())

n =  math.ceil(Decimal(a) / Decimal(b))



print(n)