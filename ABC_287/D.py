S = input()
T = input()

ls = len(S)
lt = len(T)

S_a = []
T_a = []

for i in range(ls):
    if S[i] != '?': S_a.append(i)
for i in range(lt):
    if T[i] != '?': T_a.append(i)

for i in range(len(T)+1):
    l = i
    r = ls - (lt - i)
    # for j in range(l):
    #     if j in S_a or j in T_a: continue
    #     elif S[j] == T[j]: continue
    #     else: 
    #         print ('No')
    #         break
    for j in S_a: 
        if j < l: 
            
    for 

