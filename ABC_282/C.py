n = int(input())
S = list(input())

flag = True

for i in range(n):
    if S[i] == '"' :
        flag = not flag
    if S[i] == ',' and flag == True :
        S[i] = "."

print(''.join(S))

