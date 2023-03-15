# 가르침

import sys
input = sys.stdin.readline
from collections import defaultdict


n, k = map(int, input().split())
k = k - 5
words_ = ['a', 'n', 't', 'i', 'c']
words = defaultdict()

def check_word(word):
    temp = set()
    for s in word:
        if word in words:
            pass
        else:
            temp.add(s)
    for i in temp:
        if not words.get(i):
            words[i] = 1
        else:
            words[i] += 1

for _ in range(n):
    string = input()[4:-5]
    check_word(string)

print(words)