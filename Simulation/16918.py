# 봄버맨

# R x C 직사각형 격자판 - 주변 3초 이후 폭발
# 1초 아무것도 안함, 1초 모든 칸에 폭탄 설치
# 1초 - 3초전 모든 폭탄 폭파
# 1초 빈칸에 폭탄 설치

import sys
input = sys.stdin.readline

R, C, N = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]

time_cnt = 1    # 1초 전엔 아무 일도 안 일어나
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
bomb = []

def boom(x, y):
    arr[y][x] = '.'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            arr[ny][nx] = '.'

while time_cnt < N:
    time_cnt += 1
    # 2초
    if time_cnt % 2 == 0:
        for j in range(R):
            for i in range(C):
                if arr[j][i] == 'O':
                    bomb.append((i, j))
                else:
                    arr[j][i] = 'O'
    else:
        for x, y in bomb:
            arr[y][x] = '.'
            boom(x, y)
        # 다음 과정에서 다시 폭탄 처리 할 거니까 초기화
        bomb = []

for j in range(R):
    print(*arr[j], sep='')