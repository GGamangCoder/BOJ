# Domitory Clean Problem
# 영우의 기숙사 청소 문제
# solution - 홀/짝 구분(순서 왓다갓다)

def bfs():
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]
    day = 0
    global cnt
    
    while queue:
        x, y = queue.pop(0)
        
        if day >= cnt:
            break
        spread = False      # 바이러스 퍼지는 여부
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < N):
                # 다음 과정이므로 day + 1
                if virus[nx][ny][(day+1)%2] == True:
                    continue
                virus[nx][ny][(day+1)%2] = True
                day += 1
                queue.append((nx, ny))
                spread = True
        if not spread:
            virus[x][y][((day-1)%2)]=False
                
# Input - User
N, M, K, cnt = map(int, input().split())
virus = [[[False]*2 for _ in range(N)] for _ in range(N)]   # 방 상태 - 바이러스 홀/짝 일수
queue = []
insp = []

for i in range(M):
    x, y = map(int, input().split())
    virus[x-1][y-1][0] = True
    queue.append((x-1, y-1))

for i in range(K):
    x, y = map(int, input().split())
    insp.append((x-1, y-1))

bfs()
print(virus)
# Output - Print
ans = 'NO'
for x, y in insp:
    if virus[x][y][cnt % 2] == True:
        ans = 'YES'
        break
print(ans)