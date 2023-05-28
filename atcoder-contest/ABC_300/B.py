import numpy as np

h, w = map(int, input().split())

A = [list(input()) for _ in range(h)]
B = [list(input()) for _ in range(h)]

tag = 0

Ac = []
Bc = []

for a, b in zip(A, B):
    Ac.append(str(a.count('#'))+","+str(a.count('.')))
    Bc.append(str(b.count('#'))+","+str(b.count('.')))


# for a in Ac:
#     if a not in Bc:
#         tag = 0
#         print('No')
#         break
#     else:
#         Bc.remove(a)

hs = 0
ws = 0


if Ac == Bc:
    tag = 1
else:
    for i in range(h+1):
        hs+=1
        Bc = np.roll(Bc, -1)
        # print(Ac)
        # print(Bc)
        if (Ac == Bc).all():
            tag = 1
            break


if tag:

    tag = 0

    A_w = []
    B_w = []

    A_wc = []
    B_wc = []

    for i in range(w):
        tmp = []
        for j in range(h):
            tmp.append(A[j][i])
        A_w.append(tmp)
        tmp = []
        for j in range(h):
            tmp.append(B[j][i])
        B_w.append(tmp)

    for a, b in zip(A_w, B_w):
        A_wc.append(str(a.count('#'))+","+str(a.count('.')))
        B_wc.append(str(b.count('#'))+","+str(b.count('.')))
    
    if A_wc == B_wc:
        tag = 1
    else:
        for i in range(w+1):
            ws+=1
            B_wc = np.roll(B_wc, -1)
            # print(A_wc)
            # print(B_wc)
            if (A_wc == B_wc).all():
                tag = 1
                break
    
if tag:
    for a in A:
        a = np.roll(a, -ws)
    for b in B:
        b = np.roll(b, -hs)
    print(A)
    print(B)
    if A == B:
        print('Yes')
    else:
        print('No')
else:
    print('No')