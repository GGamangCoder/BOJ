import sys
#input = sys.stdin.readline

def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x,y)]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    # 이동하는 칸에 지금까지 움직인 카운트 얹기
                    graph[nx][ny] = graph[x][y]+ 1

    return graph[N-1][M-1]

N, M = map(int, input().split())
graph, ans = [], 0

for i in range(N):
    graph.append(list(map(int, input())))

print(bfs(0,0))
