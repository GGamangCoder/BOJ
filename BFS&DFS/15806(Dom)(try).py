# Domitory Clean Problem
# 영우의 기숙사 청소 문제

def bfs(x, y, arr):
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]
    arr[x][y] = 0
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        
        if (0 <= nx < N) and (0 <= ny < N):
            if arr == temp:
                graph.append((nx, ny))
                arr[nx][ny] = 1
            elif arr == graph:
                temp.append((nx, ny))
                arr[nx][ny] = 1

# Input - User
N, M, K, cnt = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]   # 방 상태
insp = [[0 for _ in range(N)] for _ in range(N)]    # 검사 구역
temp = [[0 for _ in range(N)] for _ in range(N)]   # 새로운 곰팡이

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1

for i in range(K):
    x, y = map(int, input().split())
    insp[x][y] = 1

for i in range(1, cnt+1):
    for x in range(N):
        for y in range(N):
            if i % 2 == 1:
                if graph[x][y] == 1:
                    bfs(x, y, graph)
            else:
                if temp[x][y] == 1:
                    bfs(x, y, temp)

if cnt % 2 == 1:
    state = graph
else:
    state = temp
print(state)
# Output - Print
ans = 'NO'
for x in range(N):
    for y in range(N):
        if insp[x][y] == state[x][y] == 1:
            ans = 'YES'
print(ans)