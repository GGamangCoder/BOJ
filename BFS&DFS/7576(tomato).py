import sys
input = sys.stdin.readline

# function declare
def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1    

# Input 
N, M = map(int, input().split())
graph, queue = [], []
ans = 0

for i in range(M):
    graph.append(list(map(int, input().split())))
    
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i, j))

# Output
print(graph)
bfs()
print(graph)
# print(list(map(max, graph)))
# ans = max(map(max, graph)) -1
# for i in graph:
#     if 0 in i:
#         ans = -1
# print(ans)