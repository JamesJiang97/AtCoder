from dataclasses import dataclass
from operator import mul
from string import ascii_lowercase
from typing import List, Union
from collections import defaultdict
from functools import reduce


S = input()
len_S = len(S)


ans = defaultdict(int)


@dataclass
class Num:
    val: int
    level: int = 0

    def append(self, value: str):
        self.val = self.val * 10 + int(value)


@dataclass
class Alpha:
    val: str

    def append(self, value: str):
        self.val += value


@dataclass
class Left:
    ...


@dataclass
class Right:
    ...


token: List[Union[Left, Right, Num, Alpha]] = []


for i in range(len_S):
    cur = S[i]

    if cur.isdigit():
        if token and isinstance(token[-1], Num):
            token[-1].append(cur)
        else:
            token.append(Num(int(cur)))
    if cur.isalpha():
        token.append(Alpha(cur))
    if cur == "(":
        token.append(Left())
    if cur == ")":
        token.append(Right())

stack: List[Num] = []
cur_level = 0
for t in token:
    if isinstance(t, Left):
        cur_level += 1
    if isinstance(t, Right):
        cur_level -= 1
        stack = [x for x in stack if x.level < cur_level]
    if isinstance(t, Alpha):
        for c in t.val:
            ans[c] += reduce(mul, [x.val for x in stack], 1)
        stack = [x for x in stack if x.level < cur_level]
    if isinstance(t, Num):
        stack.append(Num(t.val, cur_level))
for i in ascii_lowercase:
    print(i, ans[i])