n = int(input())

A = list(map(int, input().split()))

E = []
O = []

for i in A:
    if i%2 == 0 : E.append(i)
    else: O.append(i)

list.sort(E, reverse=True)
list.sort(O, reverse=True)

if len(O)<2 and len(E)<2:
    print("-1")
elif len(O)<2 and len(E)>=2:
    print(E[0]+E[1])
elif len(O)>=2 and len(E)<2:
    if (O[0]+O[1])%2: print("-1")
    else :print(O[0]+O[1])
else: 
    if (E[0]+E[1])>(O[0]+O[1]):print(E[0]+E[1])
    else:
            if (O[0]+O[1])%2: print(E[0]+E[1])
            else :print(O[0]+O[1])

