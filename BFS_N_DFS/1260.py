import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())    # 1 ~ N
    graph[x][y] = graph[y][x] = 1       # graph[row][col], row: 행(가로)/col: 열(세로)
    
def dfs(V):     # x 기준으로 생각하자(V = x)
    visited = [False]*(N+1)
    stack = [V]
    while stack:
        node = stack.pop(-1)
        if visited[node] == False:
            print(node, end = ' ')
            visited[node] = True
        for idx in range(len(graph[node])-1, -1, -1):
            if graph[node][idx] == 1 and visited[idx] == False:
                stack.append(idx)

def bfs(V):
    visited = [False]*(N+1)
    queue= [V]
    while queue:
        node = queue.pop(0)
        if visited[node] == False:
            print(node, end=' ')
            visited[node] = True
            for idx in range(len(graph[node])):
                if graph[node][idx] == 1 and visited[idx] == False:
                    queue.append(idx)
       
dfs(V)
print('')
bfs(V)
