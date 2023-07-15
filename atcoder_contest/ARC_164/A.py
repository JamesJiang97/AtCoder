import numpy as np


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    ternary = list(np.base_repr(n, base=3))
    l = sum([int(i) for i in ternary])
    if k >= l and k<= n:
        print("Yes")
    else:
        print("No")
        
