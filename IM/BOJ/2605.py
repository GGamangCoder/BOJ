# 줄 세우기

from collections import deque

N = int(input())
number = list(map(int, input().split()))
line = deque()

for i in range(1, N+1):
    line.insert(i - number[i-1] - 1, i)

print(' '.join(list(map(str, line))))