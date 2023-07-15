
a, b = map(int, input().split())

ans = 0

if a<b:
    a, b = b, a

while b>0:
    ans += a//b
    a = a%b
    a, b = b, a
    
print(ans-1)