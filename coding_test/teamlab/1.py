a, b, c = 1, 0, 5

for i in range(4,49) :
    d = a + c
    a = b
    b = c
    c = d

print(c)