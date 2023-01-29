## 10815 와 동일한 문제
## hash set and map

import sys, collections
input = sys.stdin.readline

N = int(input())
# 반환 형태는 count가 많은 순으로
dict = collections.Counter(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for cnt in B:
    print(dict[cnt], end = ' ')