n, m, h, k = map(int, input().split())

S = input()

item = [list(map(int, input().split())) for _ in range(m)]

now = [0,0]

# print(item)

for s in S:
    if s == "U":
        now = [now[0], now[1]+1]
    elif s == "D":
        now = [now[0], now[1]-1]
    elif s == "R":
        now = [now[0]+1, now[1]]
    elif s == "L":
        now = [now[0]-1, now[1]]
    h -= 1
    # print(h)
    if h < 0:
        print("No")
        exit()
    if now in item:
        if h < k:
            h = k
            item.remove(now)

print("Yes")