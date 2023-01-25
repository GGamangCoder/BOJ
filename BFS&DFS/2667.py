# 단지번호 붙이기

from collections import deque

N = int(input())
graph = []
house_size = []
for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited = []
    visited.append((x, y))
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited.append((nx, ny))
                    graph[nx][ny] = 0
    return visited

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            visited = bfs(i, j)
            house_size.append(len(visited))

print(len(house_size))
house_size = sorted(house_size)
for num in house_size:
    print(num)