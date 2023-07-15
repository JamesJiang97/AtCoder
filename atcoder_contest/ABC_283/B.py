n = int(input())
A = list(map(int, input().split()))
q = int(input())
dict ={}

for i in range(q):
    inp = list(map(int, input().split()))
    # print(inp)
    if inp[0] == 1:
        if inp[1] in dict:
            dict[inp[1]] = inp[2]
        else:
            dict.update({inp[1]: inp[2]})
    else:
        if inp[1] in dict:
            print(dict[inp[1]])
        else:
            print(A[inp[1]-1])
