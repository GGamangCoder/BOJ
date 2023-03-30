# Domitory Clean Problem
# 영우의 기숙사 청소 문제

from collections import deque
import sys
input = sys.stdin.readline

# Input - User
N, M, K, t = map(int, input().split())
# 입력을 받되 홀수 날(1)과 짝수 날(0) 체크
virus = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]
q = deque()
for _ in range(M):
    x, y = map(int, input().split())
    q.append((x-1, y-1, 0))
    virus[0][y-1][x-1] = True

# 검사할 영역
ins = []
for _ in range(K):
    x, y = map(int, input().split())
    ins.append((x-1, y-1))


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
while q:
    # day 0부터 시작,
    x, y, day = q.popleft()
    
    if day >= t:
        # 이거 리턴으로 해도 상관없지 않나?
        continue
    
    next = (day+1) % 2
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue

        if virus[next][ny][nx] == False:
            virus[next][ny][nx] = True
            q.append((nx, ny, day + 1))
    else:       # 아무일도 일어나지 않는 경우, 번지지 않을 경우,
        virus[day%2][y][x] = 0


day = t % 2
for i, j in ins:
    if virus[day][j][i] == True:
        print("YES")
        break
else:
    print("NO")