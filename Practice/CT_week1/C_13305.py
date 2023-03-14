# 주유소

import sys
input = sys.stdin.readline

N = int(input())
loads = list(map(int, input().split()))     # 크기 N-1
oils = list(map(int, input().split()))      # 크기 N

res = 0
cost = oils[0]
for i in range(N-1):
    temp = oils[i]
    if cost > temp:
        cost = temp
    res += cost * loads[i]

print(res)