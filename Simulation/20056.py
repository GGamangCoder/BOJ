# 마법사 상어와 파이어볼
# 어른 상어 -> 마법사 상어

# N+2 * N+2 격자에, 파이어볼 M 개
# i번 위치 - (ri, ci), 질량 mi, 방향 di, 속력, si 
# 모든 파이어볼 방향과 속력대로 이동(한칸에 여러개 가능)
# 같은 칸의 파이어볼 하나로 합쳐짐 - 4개로 나누어짐

# 1. 질량 - 합질량/5
# 2. 속력 - 속력합/갯수
# 3. 방향 - 모두 홀수거나 짝수면 0, 2, 4, 6 / 아니면 1, 3, 5, 7
# * 질량이 0이면 소멸

# K 번 이동 -> ans; 남은 질량 합

# 크기, 갯수, 이동 횟수
N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
# 방향 (0, 1, 2, 3, 4, 5, 6, 7)
d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
# 그래프에 현재 파이어볼 상태 담아주기
for i in range(M):
    row, col, mass, vel, dir =\
        map(int, input().split())
    graph[row-1][col-1].append([mass, vel, dir])
# K번의 이동 동작 수행
def moving():
    global graph
    arr = [[[] for _ in range(N)] for _ in range(N)]
    # 모든 좌표들에 대해서
    for i in range(N):
        for j in range(N):
            for k in range(len(graph[i][j])):
                ni = (i + d[graph[i][j][k][2]][0] * graph[i][j][k][1]) % N
                nj = (j + d[graph[i][j][k][2]][0] * graph[i][j][k][1]) % N
                # 해당 정보는 그대로 넘어가기
                arr[ni][nj].append([graph[i][j][k]])
    graph = arr     # 다시 덧입혀주기

# 합쳐졌다가 분해되는 것에 대한 계산
# arr = graph[row][col] # 타입은 []
def seperate(arr):      # 특정 좌표에 담겨있는 리스트
    cnt = len(arr)      # 합쳐지는 파이어볼 갯수
    m = v = temp1 = temp2 = 0     # 질량, 속력, 홀/짝
    for i in range(cnt):
        m += arr[i][0]
        v += arr[i][1]
        # 방향에 대한 조사
        if arr[i][2] % 2 == 0:      # 짝수
            temp2 += 1
        else:
            temp1 += 1
    m //= 5
    if m == 0:
        return
    v //= cnt
    if temp1 == cnt or temp2 == cnt:        # 모두 홀/짝
        new_arr = [[m, v, i] for i in range(0, 8, 2)]
    else:
        new_arr = [[m, v, i] for i in range(1, 8, 2)]
    return new_arr

# 이동 후에 혹시 겹치는 부분 있는지 체크해주는 부분
for _ in range(K):
    moving()
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 1:
                graph[i][j] = seperate(graph[i][j])

print(graph)
res = 0
for i in range(N):
    for j in range(N):
        print(graph[i][j])
        if graph[i][j]:
            res += graph[i][j][0]
print(res)