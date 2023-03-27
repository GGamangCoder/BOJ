# 스타트 링크

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)


def bfs(s, g):
    q = [s]
    visited = [0] * (F + 1)
    visited[s] = 1
    
    while q:
        new = q.pop(0)
        if new == g:
            return visited[g]-1
        
        up = new + U
        down = new - D
        if up <= F and not visited[up]:
            q.append(up)
            visited[up] = visited[new] + 1
        if down >= 1 and not visited[down]:
            q.append(down)
            visited[down] = visited[new] + 1
    else:
        return 'use the stairs'

print(bfs(S, G))