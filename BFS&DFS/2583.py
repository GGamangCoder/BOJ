M, N, K = map(int, input().split())
space_list = []
graph = [[1 for _ in range(N)] for _ in range(M)]
cnt = 0

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x, y)]
    graph[x][y] = 0
    area = 1

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0<=nx<M) and (0<=ny<N):
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
                    area += 1
    space_list.append(area)


for _ in range(K):
    fy, fx, ly, lx = map(int, input().split())
    for x in range(fx, lx):
        for y in range(fy, ly):
            graph[x][y] = 0
            
for x in range(M):
    for y in range(N):
        if graph[x][y] == 1:
            bfs(x, y)
            cnt += 1

print(cnt)
for i in sorted(space_list):
    print(i, end=' ')
