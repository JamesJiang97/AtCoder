

import math


def solution(A, B, K) :
    return (math.floor(B/K) - math.ceil(A/K)) + 1
            


A = 6
B = 11
K = 2


print(solution(A, B, K))