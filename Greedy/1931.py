# 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
time = [tuple(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))
print(time)

cnt = end = 0
for t in time:
    if t[0] >= end:
        cnt += 1
        end = t[1]

print(cnt)