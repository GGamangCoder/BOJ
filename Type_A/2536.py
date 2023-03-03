# 버스 갈아타기

# m * n (1,1) ~ (m,n)
# k 개의 운행 버스

import sys
from collections import deque
input = sys.stdin.readline


m, n = map(int, input().split())
k = int(input())
# 가장 겉에 껍질 리스트 있다는 거 항상 생각 !!!
# 0 행, 0열 빈 리스트(패딩)
arr = [[[] for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        for j in range(y1, y2+1):
            arr[j][x1].append(b)
    elif y1 == y2:
        for i in range(x1, x2+1):
            arr[y1][i].append(b)
sx, sy, ex, ey = map(int, input().split())


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 버스 찾아가기
def bfs(x, y, bus, cnt):
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    # 네 가지 정보 큐에 저장   
    q = deque([])
    q.append([x, y, bus, cnt])
    while q:
        x, y, b, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 답 구하기
            if nx == ex and ny == ey:
                return cnt

            if 0 < nx <= m and 0 < ny <= n and b in arr[ny][nx] and not visited[ny][nx]:
                for k in range(len(arr[ny][nx])):
                    # 이전에서 같은 버스를 탔다면
                    if arr[ny][nx][k] == b:
                        q.append([nx, ny, b, cnt])  # cnt 그대로
                    else:
                        q.append([nx, ny, arr[ny][nx][k], cnt+1])
                    visited[ny][nx] = True

res = []
for bus in range(len(arr[sy][sx])):
    # 처음 시작 지점에서 탈 수 있는 버스에 대해서 탐색을 시작
    res.append(bfs(sx, sy, arr[sy][sx][bus], 1))

# 가능한 버스 숫자를 담은 리스트 중에서 최솟값, 최소환승
print(res)
print(min(res))