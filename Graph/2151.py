# 거울설치 - bfs
# 빛의 진행방향에 대해 거울 만난 후 다음 진행 방향은 두 가지가 가능
# 상, 하 <-> 좌, 우


from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [list(input()) for _ in range(N)]
# 거울 위치,시작과 끝
pos = []
for j in range(N):
    for i in range(N):
        if graph[j][i] == "#":
            pos.append((i, j))

# 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 처음 시작을 기준으로 세팅, 모든 방향 가능
dq = deque([[pos[0], 0, i] for i in range(4)])
goal_x, goal_y = pos[1][0], pos[1][1]

while dq:
    (x, y), cnt, d = dq.popleft()
    nx, ny = x + dx[d], y + dy[d]
    
    # 영역 내에서만 이루어지도록.
    while 0 <= nx < N and 0 <= ny < N and graph[ny][nx] != '*':
        # 거울 만났을 때,
        # 추가 - 그 거울에 다시 오게 될 일은 없다,
        # 만약 돌아온다면 그건 무한 루프, 거울에 빛이 갇히게 되는 경우이므로 (문제조건 위반)
        if graph[ny][nx] == "!":
            # 좌/우
            if d < 2:
                dq.append([(nx, ny), cnt+1, 2])
                dq.append([(nx, ny), cnt+1, 3])
            else:
                dq.append([(nx, ny), cnt+1, 0])
                dq.append([(nx, ny), cnt+1, 1])

        if nx == goal_x and ny == goal_y:
            dq = []
            break
        
        # 현재 진행방향으로 계속 이동, 벽 만나기 전까지 + 거울 전까지
        nx += dx[d]
        ny += dy[d]

print(cnt)