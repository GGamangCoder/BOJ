# Domitory Clean Problem
# 영우의 기숙사 청소 문제
# solution - 홀/짝 구분(순서 왓다갓다)

from collections import deque

def bfs():
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]
    day = 0
    global cnt
    
    while queue:
        x, y, day = queue.popleft()
        
        if day >= cnt:
            continue

        spread = False      # 곰팡이 퍼지는 여부
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                if virus[nx][ny][(day+1)%2] == True:
                    continue
                virus[nx][ny][(day+1)%2] = True
                queue.append((nx, ny, day+1))
                spread = True
        # 곰팡이 못 퍼지면 그 자리 끝
        if not spread:
            virus[x][y][(day%2)]=False

# Input - User
N, M, K, cnt = map(int, input().split())
virus = [[[False]*2 for _ in range(N)] for _ in range(N)]   # 방 상태 - 곰팡이 홀/짝 일수
queue = deque([])
insp = []

for i in range(M):
    x, y = map(int, input().split())
    virus[x-1][y-1][0] = True
    queue.append((x-1, y-1, 0))

for i in range(K):
    x, y = map(int, input().split())
    insp.append((x-1, y-1))

bfs()
# Output - Print
ans = 'NO'
for x, y in insp:
    if virus[x][y][cnt % 2] == True:
        ans = 'YES'
        break
print(ans)