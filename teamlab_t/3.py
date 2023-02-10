count = 0

for i in range(50000000):
    s = str(i)
    if '1' in s and i % 3 != 0 and i % 5 != 0 :
        count += s.count('1')

print(count)