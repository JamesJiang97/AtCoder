n, a, b = map(int, input().split())
C = list(map(int, input().split()))

for i in range(len(C)):
    if C[i] == a+b:
        print(i+1)
        