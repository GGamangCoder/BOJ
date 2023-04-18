# 외판원 순회 2(TSP)
# BF, 백트래킹

import sys
input = sys.stdin.readline

def dfs(start, end, sumValue, cnt):
    global minValue
    # 모든 순회 끝내고 돌아갈 때 체크
    if cnt == n:
        if graph[end][start]:
            sumValue += graph[end][start]
            if minValue > sumValue:
                minValue = sumValue
        return

    if minValue < sumValue:
        return

    for next in range(n):
        if not visited[next] and graph[end][next]:
            visited[next] = 1
            dfs(start, next, sumValue + graph[end][next], cnt+1)
            visited[next] = 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
minValue = sys.maxsize

visited = [0] * n
# 여기서 틀렸었음. - 시작 지점이 랜덤이므로
for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0

print(minValue)