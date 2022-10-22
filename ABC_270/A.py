a, b = map(int, input().split())

C = [0] * 3

if a == 1 :
    C[0] = 1
if a == 2 :
    C[1] = 1
if a == 3 :
    C[0] = 1
    C[1] = 1
if a == 4 :
    C[2] = 1
if a == 5 :
    C[0] = 1
    C[2] = 1
if a == 6 :
    C[1] = 1
    C[2] = 1
if a == 7:
    C[0] = 1
    C[1] = 1
    C[2] = 1
if b == 1 :
    C[0] = 1
if b == 2 :
    C[1] = 1
if b == 3 :
    C[0] = 1
    C[1] = 1
if b == 4 :
    C[2] = 1
if b == 5 :
    C[0] = 1
    C[2] = 1
if b == 6 :
    C[1] = 1
    C[2] = 1
if b == 7:
    C[0] = 1
    C[1] = 1
    C[2] = 1

c = 1 * C[0] + 2 * C[1] + 4*C[2]

print(c)