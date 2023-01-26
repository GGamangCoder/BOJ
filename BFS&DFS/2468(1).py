# 안전 영역(#2468)

from collections import deque

N = int(input())
graph = []
min_list, max_list = [], []
for i in range(N):
    graph.append(list(map(int, input().split())))
    min_list.append(min(graph[i]))
    max_list.append(max(graph[i]))
min, max = min(min_list)-1, max(max_list)

def bfs(x, y, high):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > high and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

res = 0
for lim in range(min, max):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] > lim:
                bfs(i, j, lim)
                cnt += 1
    if res < cnt:
        res = cnt
print(res)