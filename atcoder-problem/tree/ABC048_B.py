import math


a, b, x = map(int, input().split())
upper = b // x 
lower = (a-1) // x 


print(upper-lower)