# 일루미네이션 - 6각형, 존나 어려운데 ?

from collections import deque
import sys
input = sys.stdin.readline


w, h = map(int, input().split())
# 바깥쪽 0으로 패딩해주기
arr = [[0] * (w+2) for _ in range(h+2)]
visited = [[False] * (w+2) for _ in range(h+2)]
for j in range(1, h+1):
    arr[j][1:w+1] = map(int, input().split())

# 짝수 줄, 홀수 줄
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]
dy = [0, 1, 1, 0, -1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[y][x] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        
        for i in range(6):
            nx, ny = x + dx[y%2][i], y + dy[i]
            if 0 <= nx < w+2 and 0 <= ny < h+2:
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True
                elif arr[ny][nx] == 1:
                    cnt += 1
    return cnt

print(bfs(0, 0))