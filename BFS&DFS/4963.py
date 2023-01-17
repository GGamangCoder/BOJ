import sys
input = sys.stdin.readline

# 함수 정의 - BFS
def bfs(x, y):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    queue = [(x, y)]
    graph[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < w) and (0 <= ny < h):
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0

while True:
    # 입력
    h, w = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt = 0
    for i in range(w):
        graph.append(list(map(int, input().split())))

    # 출력
    for i in range(w):
        for j in range(h):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
