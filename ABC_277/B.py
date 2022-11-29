n = int(input())

S = []

tag = 1

for i in range(n):
    s = input()
    if S.count(s) != 0:
        tag = 0
        break
    if s[0] != 'H' and s[0] != 'D' and s[0] != 'C' and s[0] != 'S':
        tag = 0
        break
    if s[1] != 'A' and s[1] != '2' and s[1] != '3' and s[1] != '4' and s[1] != '5' and s[1] != '6' and s[1] != '7' and s[1] != '8' and s[1] != '9' and s[1] != 'T' and s[1] != 'J' and s[1] != 'Q' and s[1] != 'K':
        tag = 0
        break
    S.append(s)

if tag : print("Yes")
else : print("No")
