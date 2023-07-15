# ID: ABC304 D
#URL: https://atcoder.jp/contests/abc304/tasks/abc304_d

import bisect

w, h = map(int, input().split())
n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

num_a = int(input())
A = list(map(int, input().split()))
num_b = int(input())
B = list(map(int, input().split()))


count = {}

for point in points:
    x, y = point
    x_axis = bisect.bisect(A, x)
    y_axis = bisect.bisect(B, y)
    if (x_axis, y_axis) in count:
        count[(x_axis, y_axis)] += 1
    else:
        count[(x_axis, y_axis)] = 1

# if (num_a+1)*(num_b+1) > n:
#     min_count = 0
# else:
#     min_count = min(count.values())

if (num_a+1)*(num_b+1) == len(count):
    min_count = min(count.values())
else:    
    min_count = 0

max_count = max(count.values())

print(str(min_count) + " " + str(max_count))
