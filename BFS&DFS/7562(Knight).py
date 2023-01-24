T = int(input())

def bfs(x, y):
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]
    queue = [(x, y)]
    
    while queue:
        x, y = queue.pop(0)
        
        if x == Fx and y == Fy:
            return graph[x][y]
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < size) and (0 <= ny < size) and (graph[nx][ny] == 0):
                # graph[x][y] 가 0이 아닌 경우는 ? 최단거리라 돌아올 일이 없나 ?
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

for test_case in range(1, T+1):
    size = int(input())
    Cx, Cy = map(int, input().split())      # 현재 위치(Current)
    Fx, Fy = map(int, input().split())      # 최종 위치(Final)
    graph = [[0 for _ in range(size)] for _ in range(size)]
    
    print(bfs(Cx, Cy))