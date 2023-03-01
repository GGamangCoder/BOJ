# Domitory Clean Problem
# 영우의 기숙사 청소 문제

from collections import deque

# Input - User
N, M, K, cnt = map(int, input().split())
virus = [[0 for _ in range(N)] for _ in range(N)]   # 방 상태
queue = deque()    # 검사 구역
insp = []   # 새로운 곰팡이

for _ in range(M):
    x, y = map(int, input().split())
    virus[x-1][y-1] = True
    queue.append((x-1, y-1, 0))

for _ in range(K):
    x, y = map(int, input().split())
    insp.append((x-1, y-1))


def bfs():
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]

    while queue:
        x, y, day = queue.popleft()
        if day > cnt:
            break

        virus[x][y] = False
        # spread = False
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < N):
                virus[nx][ny] = True
                queue.append((nx, ny, day+1))
                # spread = True

# Output - Print
bfs()
ans = 'NO'
for x, y in insp:
    if virus[x][y] == True:
        ans = 'YES'
        break
print(ans)