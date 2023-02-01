# 알파벳 문제

N, M = map(int, input().split())
graph = []          # 그래프 모양
for _ in range(N):
    graph.append(list(input()))

def dfs(start):     # start = (0, 0) and graph[0][0]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    stack, visited = [], []         # 가는 루트 / 방문 알파벳
    stack.append(start)
    temp = [start]
    cnt = 0
    prev_x, prev_y = 0, 0

    while stack:
        x, y = stack.pop()
        if graph[x][y] not in visited:
            visited.append(graph[x][y])

        cnt = max(cnt, len(visited))    # 2. 다만 추가될수록 visited만 증가 시 최댓값 초기화
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M):
                # 방문한 적 없으면, 직전 지점 아니면
                if graph[nx][ny] not in visited and (prev_x, prev_y) != (nx, ny):
                    # if (x, y) not in temp:
                    #     temp.append((x, y)) #######
                    stack.append((nx, ny))
                    temp.append((nx, ny))
                    visited.append(graph[nx][ny])
                    print('#add', stack, temp, visited)
                    break
            if i == 3 and temp != []:
                if (x, y) == temp[-1]:
                    prev_x, prev_y = temp.pop() # 끝 지점
                    visited.pop()
                    print('#back_mid', stack, temp, visited)
                # if temp != []:
                #     x, y = temp.pop()           # 이전 지점
                stack.append(temp[-1])        # 이전 지점 스택 추가
                print('#back', stack, temp, visited)
    return cnt

print(dfs((0,0)))