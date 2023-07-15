import bisect

n = int(input())
A = list(map(int, input().split()))
q = int(input())

sleep_time = [0]

for i in range(1, n):
    if (i+1) % 2 == 0:
        sleep_time.append(sleep_time[i-1])
    else:
        sleep_time.append(sleep_time[i-1] + (A[i] - A[i-1]))


for _ in range(q):
    l, r = map(int, input().split())
    a1 = bisect.bisect_right(A, l)
    a2 = bisect.bisect_right(A, r)

    ans = sleep_time[a2-1] - sleep_time[a1-1] + (A[a1-1] - l) * ((a1+1) % 2) + (r - A[a2-1]) * ((a2+1) % 2)
    print(ans)