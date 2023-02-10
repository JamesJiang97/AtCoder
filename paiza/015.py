# k, s, t = map(int, input().split())

def gen(k):
    if k == 1: return 'ABC'
    else: return 'A'+gen(k-1) + 'B' + gen(k-1) + 'C'

print (gen())