# 동전 0

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0]*N
for i in range(N):
    coins[i] = int(input())

cnt = 0
while K != 0:
    for i in range(N-1, -1, -1):
        coin = coins[i]
        cnt += K // coin
        K %= coin

print(cnt)