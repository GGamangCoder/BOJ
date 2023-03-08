# 동전 2

# n가지의 동전 -> k원
# 결과는 가능한 최소 갯수, 불가능 -1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
    coins[i] = int(input().strip())

# 경우의 수를 담는 dp 생성, 밑에서 최솟값 갱신하므로 최대값으로 초기화
dp = [10001] * (k+1)
# dp[0] = 0
# 모든 코인 경우에 따라서
for coin in coins:
    for i in range(coin, k+1):
        # 새로운 것이 그 코인을 포함하는지에 따라 최솟값 갱신
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])