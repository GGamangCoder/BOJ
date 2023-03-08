# 빙산

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 빙하가 있는 위치와 양을 딕셔너리로
ice = {}
for j in range(n):
    for i in range(m):
        if arr[j][i]:
            ice[(i, j)] = arr[j][i]

# 빙하 녹는 방향 체크
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 빙하를 녹이도록 체크하는 함수
def bfs(x, y):
    q = deque([(x, y)])
    visited[y][x] = True
    
    while q:
        x, y = q.popleft()
        sea = 0             # 빈 바다 영역
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                # 바다에 접해있을 때,
                if not arr[ny][nx]:
                    sea += 1
                # 체크 안한, 붙어있는 빙산일 경우
                elif arr[ny][nx] and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
        if sea > 0:
            left_ice = max(0, ice[(x, y)] - sea)
            ice[(x, y)] = left_ice
    for i, j in ice.keys():
        arr[j][i] = ice[(i, j)]

    return 1        # 1회 끝나면 한 뭉탱이


ans = 0
while ice:
    visited = [[False]*m for _ in range(n)]
    temp = 0        # 빙하 뭉탱이
    for p in ice.keys():  # 빙하 좌표
        x, y = p
        if not visited[y][x]:
            temp += bfs(x, y)
    # ans += 1
    if temp > 1:
        print(ans)
        break
    lst = []
    for p in ice.keys():
        if ice[p] == 0:
            lst.append(p)
    for i in lst:
        del ice[i]
    # 위에서 해주면 반복이 한 번씩 더 돌아서 여기서 체크를 해야한다. 이유는?
    ans += 1

if temp < 2:
    print(0)