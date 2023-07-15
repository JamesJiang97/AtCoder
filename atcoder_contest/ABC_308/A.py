S = list(map(int, input().split()))

for i in range(len(S)-1):
    if S[i+1]>=S[i]:
        continue
    else:
        print('No')
        exit()

for i in range(len(S)):
    if S[i]<100 or S[i]>675:
        print('No')
        exit()
    if S[i]%25!=0:
        print('No')
        exit()

print('Yes')

