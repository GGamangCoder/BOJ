# 알파벳 문제

N, M = map(int, input().split())
graph = []          # 그래프 모양
for _ in range(N):
    graph.append(list(input()))

def dfs(start):     # start = (0, 0) and graph[0][0]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    stack, visited = [], []         # 가는 루트 / 방문 알파벳
    stack.append(start)
    branch = {(0, 0): []}
    cnt = 0
    prev_x, prev_y = 0, 0

    while stack:
        x, y = stack[-1]
        if graph[x][y] not in visited:
            visited.append(graph[x][y])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                # 방문한 적 없으면, 직전 지점 아니면
                if graph[nx][ny] not in visited and (prev_x, prev_y) != (nx, ny):
                    if (x, y) in branch.keys():
                        if i in branch[(x, y)]:
                            continue
                        branch[(x, y)].append(i)
                    else:
                        branch[(x, y)] = [i]
                    stack.append((nx, ny))
                    visited.append(graph[nx][ny])
                    break
            if i == 3 and stack != []:
                prev_x, prev_y = stack.pop() # 끝 지점
                cnt = max(cnt, len(visited))    # 2. 다만 추가될수록 visited만 증가 시 최댓값 초기화
                visited.pop()
                if (prev_x, prev_y) in branch.keys():
                    del branch[(prev_x, prev_y)]

    return cnt

print(dfs((0,0)))