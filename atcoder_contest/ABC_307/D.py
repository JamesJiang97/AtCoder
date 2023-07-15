from collections import deque

n = int(input())

S = deque(list(input()))

stack = deque()

c_count = 0

for i in range(n):
    s = S.popleft()

    if s == "(":

        c_count += 1
        stack.append(s)
        del_count = 0
    elif s == ")":
        if c_count == 0:
            stack.append(s)
        else:
            pop_s = s
            stack.append(s)
            while pop_s != "(":
                pop_s = stack.pop()
            c_count -= 1

    else:
        stack.append(s)
print("".join(stack))