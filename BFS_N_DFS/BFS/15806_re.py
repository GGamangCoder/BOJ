import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

n, m, k, t = map(int, input().split())

mold = deque()
for _ in range(m):
    mold.append(tuple(map(int, input().split())))

# 좌표가 1,1부터 시작하므로 n+1까지 선언
# 해당 위치에 도달하는데 불가능한 경우는
# t일 이후에 도달한다는 의미로 max(t)+1로 초기화
# 한 위치에서 번식이 되었으면, 2일 간격으로 생성되거나 사라진다.
# 그래서 홀수 최단거리, 짝수 최단거리를 구한다.
room = [[[10001 for _ in range(n+1)] for _ in range(n+1)] for _ in range(2)]

# x,y에 거리 0을 추가해서 저장
# 초기 곰팡이는 1일후 어차피 모두 사라지므로 초기화 x
# 2일차때 초기 위치로 돌아오는 곰팡이만 계속 반복해서 생성되고 사라짐
for i in range(m):
    x, y = mold[i]
    mold[i] = (x, y, 0)

# 청소 검사날 체크하는 위치 리스트
check_area = [list(map(int, input().split())) for _ in range(k)]


while mold:
    x, y, dis = mold.popleft()

    if dis >= 10001:
        break

    for dir in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx <= 0 or nx > n or ny <= 0 or ny > n:
            continue

        # 해당영역에 짝수번째, 홀수번째 일째에서 이전에 도달 했는지 체크하기
        if room[(dis + 1) % 2][nx][ny] == 10001:
            room[(dis + 1) % 2][nx][ny] = dis + 1
            mold.append((nx, ny, dis + 1,))


check_clean = False
for x, y in check_area:
    if room[t % 2][x][y] <= t:
        check_clean = True
        break

if check_clean:
    print("YES")
else:
    print("NO")