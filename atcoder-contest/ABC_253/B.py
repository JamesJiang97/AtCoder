h, w = map(int, input().split())

mas = []

for i in range(h) :
    s = input()
    for j in range(w) :
        if s[j] == "o" :
            mas.append(i)
            mas.append(j)

ans = abs(mas[0] - mas[2]) + abs(mas[1]-mas[3])

print(ans)