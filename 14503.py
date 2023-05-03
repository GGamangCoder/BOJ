n, m = map(int, input().split())

# 청소 여부
v = [[0]*m for _ in range(n)]
x, y, direc = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

def turn_left():
    global direc
    direc -= 1  # 왼쪽 이동
    if direc == -1: # 음수되면 3으로 초기화
        direc = 3

v[y][x] = 1
cnt = 1     # 처음 위치 카운트
turn_time = 0       # 왼쪽 회전 방향 횟수 카운트
while True:
    turn_left()
    nx, ny = x + dx[direc], y + dy[direc]
    
    if v[ny][nx] == 0 and graph[ny][nx] == 0:
        v[ny][nx] = 1       # 해당 위치 청소
        x, y = nx, ny       # 위치 이동
        cnt += 1
        turn_time = 0       # 왼 방향 회전 횟수 초기화
        continue
    
    else:       # 불가능하면 왼쪽 방향 회전
        turn_time += 1
    
    if turn_time == 4:
        nx, ny = x - dx[direc], y - dy[direc]
        
        if graph[ny][nx] == 0:
            x, y = nx, ny
        else:
            break
        
        turn_time = 0

print(cnt)