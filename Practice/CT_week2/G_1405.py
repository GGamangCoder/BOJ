# 미친 로봇

# 방향 = E W N S(동 서 북 남)
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def dfs(x, y, cnt, p):
    global ans
    if cnt == n:
        ans += p       # 끝까지 간 경우 확률 더하기
        return
    
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < (2*n + 1) and 0 <= ny < (2*n + 1):
            if not graph[ny][nx]:
                graph[ny][nx] = 1
                dfs(nx, ny, cnt+1, p*ratio[i])
                graph[ny][nx] = 0

condition = list(map(int, input().split()))
n = condition[0]
ratio = [condition[i]/100 for i in range(1, 5)]
ans = 0

# 양쪽으로 최대 n만큼 갈 수 있으므로 최대 크기 2n+1 * 2n+1
graph = [[0]*(2*n+1) for _ in range(2*n+1)]
graph[n][n] = 1

dfs(n, n, 0, 1)
print(ans)