# 알파벳 문제

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

def dfs(start):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    stack, visited = [(0, 0)], []
    visited.append(start)
    cnt = 0
    temp = []
    flag = False
    
    while stack:
        x, y = stack.pop()
        print((x,y))
        cnt = max(cnt, len(visited))    # 2. 다만 추가될수록 visited만 증가 시 최댓값 초기화
        if not(x == 0 or y== 0) and graph[x][y] in visited:      # 1. 이미 있는거면 visited도 빼주기
            visited.pop()
            flag = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < N) and (0 <= ny < M) and graph[nx][ny] not in visited:
                if flag == True:
                    continue
                stack.append((nx, ny))
                visited.append(graph[nx][ny])
                temp.append((nx, ny))
                print(stack, visited)
                break
            if i == 3:      # 끝에 지점에 다다르면 다시 분기점에서 체크
                if temp != []:
                    x, y = temp.pop()
                    stack.append((x, y))
        flag = False
                
    return cnt

print(dfs(graph[0][0]))