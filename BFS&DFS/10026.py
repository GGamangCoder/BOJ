## 수정 필요

import sys
input = sys.stdin.readline

# 적록색약
def inNormal():
    graph = temp[:][:]
    global cnt
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'
    color.remove('G')
    display()
#    return graph

# 함수 구현
def bfs(x, y, rgb):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(x, y)]
    graph[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if graph[nx][ny] == rgb:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0

# 입력
N = int(input())
color = ['R', 'G', 'B']
graph = []
cnt = 0
for _ in range(N):
    graph.append(list(map(str, input())))
temp = graph[:][:]

# 출력
def display():
    global cnt
    for rgb in color:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == rgb:
                    bfs(i, j, rgb)
                    cnt += 1

display()
print(cnt, end = ' ')
inNormal()
print(cnt)
