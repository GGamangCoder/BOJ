# 인구 이동 문제

import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []      # 현재 상태
for i in range(N):
    graph.append(list(map(int, input().split())))
    
def bfs(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    queue = [(x, y)]
    temp = [(x, y)]     # 인접 국경 나라
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < N) and visited[nx][ny] == 0:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    visited[nx][ny] = 1     # 체크 표시
                    queue.append((nx, ny))
                    temp.append((nx, ny))
                    
    return temp

cnt = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)] # 체크 여부
    flag = 0        # 인구 이동 여부, 0이면 이동 없어 무한 루프 종료
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i, j)
                
                if len(temp) >= 2:      # 두 나라 이상이면 인구 이동 필요
                    flag = 1
                    new_number = sum([graph[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        graph[x][y] = new_number
    
    if flag == 0:
        break
    cnt += 1

print(cnt)