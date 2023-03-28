# 파이프 옮기기 1
# DFS 풀이 - Pypy3 로 실행

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
# before 에 따라서 가로 세로 대각선
# before = 0(가로), 1(세로), 2(대각선)
def dfs(x, y, before):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    
    # 대각선 이동
    if x + 1 < N and y + 1 < N:
        if not graph[y+1][x+1] and not graph[y+1][x] and not graph[y][x+1]:
            dfs(x+1, y+1, 2)

    # 가로 이동
    if before != 1 and x + 1 < N:
        if not graph[y][x+1]:
            dfs(x+1, y, 0)

    # 세로 이동
    if before != 0 and y + 1 < N:
        if not graph[y+1][x]:
            dfs(x, y+1, 1)

# (0, 0) -> (1, 0) / 가로 방향 시작(0)
dfs(1, 0, 0)
print(cnt)