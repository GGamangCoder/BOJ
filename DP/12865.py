# 평범한 배낭
# 230412

import sys
input = sys.stdin.readline

# 물품 수 N & 최대 무게 K
N, K = map(int, input().split())

bag = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
# 가치 합이 저장됨. 1~K 무게까지, 1~N 째의 배낭
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = bag[i][0]       # 무게
        v = bag[i][1]       # 가치

        # 배낭에 담을 수 없는 경우는 그냥 처리
        if j < w:
            dp[i][j] = dp[i-1][j]
        # 배낭에 담을 수 있다면, 안 담는 경우와 담는 경우 중 가치가 높은 거에 맞춰서
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])