n = int(input())

S = input()
T = input()

for s, t in zip(S, T):
    if s == t or (s=="1" and t == "l") or (t=="1" and s == "l") or (s == "0" and t == "o") or (t == "0" and s == "o"):
        continue
    else:
        print("No")
        exit()

print("Yes")