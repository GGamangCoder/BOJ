# 1, 2, 3 더하기


import sys
input = sys.stdin.readline


dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])

T = int(input())
for tc in range(1, T+1):
    print(dp[int(input())])