import sys
input = sys.stdin.readline
from collections import deque

# function declare
def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    global queue
    
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < N:
                if graph[nx][ny][nz] == 0:
                    queue.append((nx, ny, nz))
                    graph[nx][ny][nz] = graph[x][y][z] + 1

# Input 
N, M, H = map(int, input().split())
graph, queue = [], deque([])
ans = 0

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append((i, j, k))
    graph.append(temp)

# Output 
bfs()
ans = max(map(max, graph)) -1
for i in range(H):
    for j in range(M):
        if 0 in graph[i][j]:
            ans = -1
print(ans)