S = input()
T = input()

dictS = {'@':0}
dictT = {'@':0}

keyA = ["a", "t", "c", "o", "d", "e", "r"]

for s in S:
    if s not in dictS:
        dictS[s] = 1
        if s not in dictT:
            dictT[s] = 0
    else:
        dictS[s] += 1
for t in T:
    if t not in dictT:
        dictT[t] = 1
        if t not in dictS:
            dictS[t] = 0
    else:
        dictT[t] += 1


for keyS, keyT in zip(dictS, dictT):
    if dictS[keyS] == dictT[keyT] and keyS != "@":
        dictS[keyS] = 0
        dictT[keyT] = 0
    elif keyS != "@":
        if dictS[keyS] > dictT[keyT]:
            dictS[keyS] -= dictT[keyT]
            dictT[keyT] = 0
            if keyS in keyA and dictT["@"] >= dictS[keyS]:
                dictT["@"] -= dictS[keyS]
                dictS[keyS] = 0
        elif dictS[keyS] < dictT[keyT]:
            dictT[keyT] -= dictS[keyS]
            dictS[keyS] = 0
            if keyT in keyA and dictS["@"] >= dictT[keyT]:
                dictS["@"] -= dictT[keyT]
                dictT[keyT] = 0

if dictS["@"] != dictT["@"]:
    print("No")
    exit()
else:
    dictS["@"] = 0
    dictT["@"] = 0

for valueS, valueT in zip(dictS.values(), dictT.values()):
    if valueS > 0 or valueT > 0:
        print("No")
        exit()

print("Yes")
