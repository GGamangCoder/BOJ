#백준 15806번 영우의 기숙사청소
from collections import deque
N,M,K,t=map(int,input().split())
dir=[(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]
q=deque()
check=[]
visited=[[[False]*2 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    q.append((a-1,b-1,0))
    visited[a-1][b-1][0]=True

for _ in range(K):
    c,d=map(int,input().split())
    check.append((c-1,d-1))
#바이러스는 홀/짝으로 퍼짐
#홀수일때 짝수일때 바이러스가 각각 다르다
while q:
    x,y,day=q.popleft()
    if day>=t:
        continue
    v_c=False
    for d in range(8):
        nx=x+dir[d][0]
        ny=y+dir[d][1]

        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        next=(day+1)%2
        if visited[nx][ny][next]==True:
            continue
        visited[nx][ny][next]=True
        q.append((nx,ny,day+1))
        v_c=True
    #만약 바이러스가 안퍼짐
    #-->다시 그 자리로 못온다
    #결국 그 바이러스는 없어짐
    if not v_c:
        visited[x][y][(day%2)]=False

c=t%2
for cx,cy in check:
    if visited[cx][cy][c]==True:
        print("YES")
        exit(0)

print("NO")
