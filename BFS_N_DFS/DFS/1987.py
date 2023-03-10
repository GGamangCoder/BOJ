# 알파벳 문제
# DFS를 활용한 백트래킹 - 중복되지 않는 알파벳 조건 때문에

import sys
sys.setrecursionlimit(10000) 

N, M = map(int, input().split())
graph = [list(map(lambda x: ord(x)-65, input())) for _ in range(N)]
# 방문 알파벳이 들어갈 공간, 첫 좌표부터,
# 여기에 문자를 넣으면 시간 초과가 떠서 숫자로 바꿈. 시간 복잡도 ?!
visited = [0]*26
visited[graph[0][0]] = 1
ans = 0

def dfs(x, y, cnt):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    global ans
    ans = max(cnt, ans)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if visited[graph[nx][ny]] == 0:
                visited[graph[nx][ny]] = 1
                dfs(nx, ny, cnt + 1)
                visited[graph[nx][ny]] = 0

dfs(0, 0, 1)
print(ans)