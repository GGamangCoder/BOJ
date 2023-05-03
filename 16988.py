# 바둑2 (easy)
# 바둑판 상태를 그대로 두고 두 개를 놓았을 때 상황을 체크

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    flag = True
    v[i][j] = value
    q.append([i, j])
    res = 1
    while q:
        i, j = q.popleft()
        for idx in range(4):
            ni, nj = i + di[idx], j + dj[idx]
            if 0<=ni<n and 0<=nj<m and v[ni][nj] < value:
                if arr[ni][nj] == 0:
                    flag = False
                elif arr[ni][nj] == 2:
                    v[ni][nj] = value
                    res += 1
                    q.append((ni, nj))
    return res if flag else -1
    

def set(pos):
    for i, j in pos:
        arr[i][j] = 1

def init(pos):
    for i, j in pos:
        arr[i][j] = 0


def play(pos):
    global value
    res = 0
    value += 1
    set(pos)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 and v[i][j] < value:
                cnt = bfs(i, j)
                if cnt != -1:
                    res += cnt
    init(pos)
    return res


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[-1] * m for _ in range(n)]
blank = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank.append((i, j))

value = 0
cnt = 0         # 최대 갯수
for p in combinations(blank, 2):
    cnt = max(cnt, play(p))
print(cnt)
