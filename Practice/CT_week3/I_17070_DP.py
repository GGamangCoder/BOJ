# 파이프 옮기기 1
# DP 풀이 - python3 로도 가능!

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 해당 지점까지 경우의 수 저장 - 좌표, 방향
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
# 초기 세팅, 가로(0) / 세로(1) / 대각선(2)
dp[0][1][0] = 1

# 첫 번째 행에 대해 우선 초기화 - 모두 가로
for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for j in range(1, N):
    for i in range(1, N):
        # 대각선 가능한 경우,
        if graph[j][i] == 0 and graph[j-1][i] == 0 and graph[j][i-1] == 0:
            dp[j][i][2] = dp[j-1][i-1][0] + dp[j-1][i-1][1] + dp[j-1][i-1][2]
        
        if graph[j][i] == 0:
            # 가로에 대해서
            dp[j][i][0] = dp[j][i-1][0] + dp[j][i-1][2]
            # 세로에 대해서
            dp[j][i][1] = dp[j-1][i][1] + dp[j-1][i][2]

ans = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(ans)