#백준 15806번 영우의 기숙사청소
from collections import deque

N,M,K,t=map(int,input().split())
dir=[(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]
q=deque()
check=[]
visited=[[[False]*2 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y=map(int,input().split())
    q.append((x-1,y-1,0))
    visited[y-1][x-1][0]=True

for _ in range(K):
    x, y=map(int,input().split())
    check.append((x-1,y-1))

while q:
    x, y, day = q.popleft()
    if day >= t:
        continue

    for d in range(8):
        nx = x + dir[d][0]
        ny = y + dir[d][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        next = (day + 1) % 2
        if visited[ny][nx][next] == True:
            continue
        visited[ny][nx][next] = True
        q.append((nx, ny, day+1))
    else:
        visited[y][x][(day%2)]=False

day = t % 2
for i, j in check:
    if visited[j][i][day]==True:
        print("YES")
        break
else:
    print("NO")