from decimal import Decimal, ROUND_HALF_UP

x, k = map(int, input().split())

for i in range(k):
    t = i
    x = int(Decimal(str(x)).quantize(Decimal('1E' + str(t+1)), rounding=ROUND_HALF_UP))

print(x)