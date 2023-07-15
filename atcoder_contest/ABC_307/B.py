import itertools

n = int(input())

S = []

for _ in range(n):
    S.append(input())

for l in itertools.permutations(S,2):

    s = l[0] + l[1]
    if s == s[::-1]:
        print("Yes")

        exit()

print("No")
