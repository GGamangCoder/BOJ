# Knight Moving Minimum Cnt Print Problem
# 나이트 최소 횟수 움직임 문제

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
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    Cx, Cy = map(int, input().split())      # 현재 위치(Current)
    Fx, Fy = map(int, input().split())      # 최종 위치(Final)
    graph = [[0 for _ in range(size)] for _ in range(size)]
    
    print(bfs(Cx, Cy))