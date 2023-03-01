# 음식물 피하기

import sys
input = sys.stdin.readline


def bfs(x, y):
    q = [(x, y)]
    V[y][x] = True
    cnt = 1
    while q:
        i, j = q.pop(0)
        for idx in range(4):
            ni, nj = i + d[idx][0], j + d[idx][1]
            if 1 <= ni < M+1 and 1 <= nj < N+1:
                if arr[nj][ni] == 1 and not V[nj][ni]:
                    V[nj][ni] = True
                    q.append((ni, nj))
                    cnt += 1

    return cnt

N, M, K = map(int, input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
V = [[False]*(M+1) for _ in range(N+1)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1

val = ans = 0
for i in range(1, M+1):
    for j in range(1, N+1):
        if arr[j][i] == 1:
            val = bfs(i, j)
            ans = max(val, ans)

print(ans)