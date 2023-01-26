# 안전 영역

from collections import deque
import copy

N = int(input())    # 2 <= N <= 100
graph = []
min_list, max_list = [], []
for i in range(N):
    graph.append(list(map(int, input().split())))
    min_list.append(min(graph[i]))
    max_list.append(max(graph[i]))
min, max = min(min_list)-1, max(max_list)

def bfs(x, y, high):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = deque([])
    queue.append((x, y))
    arr[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > high:       # 수정 필요
                    arr[nx][ny] = 0
                    queue.append((nx, ny))
                else:
                    arr[nx][ny] = 0

area = 0
for lim in range(min, max+1):
    cnt = 0
    arr = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if arr[i][j] > lim:
                bfs(i, j, lim)
                cnt +=1
            else:
                arr[i][j] = 0
    if area <= cnt:
        area = cnt
print(area)