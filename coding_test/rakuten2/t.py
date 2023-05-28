def solution(S):

    lS = list(str(S))

    ans = 0

    setS = set()

    for i in range(len(lS)) :
        for j in range(10):
            T = lS.copy()
            T[i] = str(j)
            # print(T)
            t = int(''.join(T))
            # print(t)
            if t % 3 == 0 and t not in setS : 
                setS.add(t)

    # print(setS)

    
    return len(setS)


S = '0081'


solution(S)
