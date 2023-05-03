# 점프

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1


for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        
        temp = arr[j][i]
        if i + temp < n:
            dp[j][i + temp] += dp[j][i]

        if j + temp < n:
            dp[j + temp][i] += dp[j][i]

print(dp[n-1][n-1])