# 가르침

import sys
input = sys.stdin.readline
from collections import defaultdict, deque


n, k = map(int, input().split())
words_ = ['a', 'n', 't', 'i', 'c']
words = defaultdict()
cnt = 0

def check_word(word):
    temp = set()
    for s in word:
        if word in words_:
            pass
        else:
            temp.add(s)
    if not temp:
        cnt += 1
    else:
        for i in temp:
            if i not in words_:
                if not words.get(i):
                    words[i] = 1
                else:
                    words[i] += 1

def solve(lst):
    global cnt
    temp = []
    if k <= 0:
        return cnt
    for idx in lst:
        temp.append(words[idx])
    temp = sorted(temp)
    for _ in range(k-5):
        cnt += temp.pop()
    return cnt

for _ in range(n):
    string = input()[4:-5]
    check_word(string)

if k < 5:
    print(0)
else:
    print(solve(words))