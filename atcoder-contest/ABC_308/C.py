from decimal import Decimal

n = int(input())


li = []

for i in range(n):
    a, b = map(int, input().split())
    s = Decimal(a)/Decimal(a+b)
    li.append((s, i+1))


ans = sorted(li, key=lambda x: (-x[0], x[1]))

for i in range(n):
    print(ans[i][1], end=" ")


# heapq.heapify(ans)

# for i in range(n):
#     a, b = map(int, input().split())
#     s = a/(a+b)
#     print(s)
#     heapq.heappush(ans, (-s, i+1))

# while len(ans) > 0:
#     print(heapq.heappop(ans)[1], end=" ")