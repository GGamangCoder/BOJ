####################
##### 단순 풀이 #####
####################
import sys
#input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
cnt = 0

for _ in range(N):
    arr.append(list(map(str, input())))

for i in range(N):
    temp = ''
    for j in range(M):
        if arr[i][j] == '-' and arr[i][j] != temp:
            cnt += 1
        temp = arr[i][j]

for j in range(M):
    temp = ''
    for i in range(N):
        if arr[i][j] == '|' and arr[i][j] != temp:
            cnt += 1
        temp = arr[i][j]

print(cnt)


####################
##### BFS 풀이 #####
####################
def bfs(x, y):
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        
        if graph[x][y] == '-':
            if (y+1) < M and graph[x][y+1] == '-':
                queue.append((x, y+1))
        elif graph[x][y] == '|':
            if (x+1) < N and graph[x+1][y] == '|':
                queue.append((x+1, y))
        graph[x][y] = -1

N, M = map(int, input().split())
graph, cnt = [], 0

for _ in range(N):
    graph.append(list(map(str, input())))

for i in range(N):
    for j in range(M):
        if graph[i][j] != -1:
            bfs(i, j)
            cnt += 1

print(cnt)

