# 점프왕 쩰리 (Small)
# 출력 결과 - 성공(HaruHaru), 실패(Hing)

# import sys
# input = sys.stdin.readline

d = [(1, 0), (0, 1)]      # 오른쪽이나 아래로 이동, (x, y)

N = int(input())        # 2 <= N <= 3

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
################################################
# 방문 여부 결정만으로 시간이 엄청나게 줄어든다..  #
################################################

stack = [(0, 0)]
ans = 'Hing'
while stack:
    x, y = stack.pop()
    if x == N-1 and y == N-1:
        ans = 'HaruHaru'
        break
    val = graph[y][x]
    for i in range(2):
        # 움직인 후의 좌표
        nx, ny = x + d[i][0] * val, y + d[i][1] * val
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = 1
            stack.append((nx, ny))
        # else:       # 범위를 넘어가면,
        #     continue    # 일단은 다음 턴으로

print(ans)