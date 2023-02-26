# 마법사 상어와 파이어볼

# N * N 격자에, 파이어볼 M 개
# i번 위치 - (ri, ci), 질량 mi, 방향 di, 속력, si 
# 모든 파이어볼 방향과 속력대로 이동(한칸에 여러개 가능)
# 같은 칸의 파이어볼 하나로 합쳐짐 - 4개로 나누어짐

# 1. 질량 - 합질량/5
# 2. 속력 - 속력합/갯수
# 3. 방향 - 모두 홀수거나 짝수면 0, 2, 4, 6 / 아니면 1, 3, 5, 7
# * 질량이 0이면 소멸

# K 번 이동 -> ans; 남은 질량 합

# 입력
# 크기, 갯수, 이동 횟수
N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
# 방향 (0, 1, 2, 3, 4, 5, 6, 7)
d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
# 그래프에 현재 파이어볼 상태 담아주기
for i in range(M):
    row, col, mass, vel, dir =\
        map(int, input().split())
    graph[row-1][col-1].append([mass, vel, dir])


# 이동에 대한 함수
def moving():
    global graph
    temp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 비어 있지 않은 graph 정보에 대해서,
            # info 는 리스트 형태, [mass, vel, dir]
            for info in graph[j][i]:
                x, y = i, j
                m_, v_, d_ = info  # 정보들
                # 1열과 N열로 연결, 돌아오므로
                nx = (x + d[d_][0]*v_) % N
                ny = (y + d[d_][1]*v_) % N
                temp[ny][nx].append([m_, v_, d_])
    temp = check_ball(temp)
    return temp

# 합쳐지는 것에 대한 처리
def check_ball(arr):
    for i in range(N):
        for j in range(N):
            cnt = len(arr[j][i])        # 정보 갯수
            if cnt > 1:
                m = v = 0           # 질량/속력,
                odd = even = True     # 홀/짝 체크
                for info in arr[j][i]:
                    m_, v_, d_ = info
                    m += m_
                    v += v_
                    # 둘 다 false 값을 가지면 방향 홀수
                    if d_ % 2 == 0:     # 짝수
                        even = False
                    elif d_ % 2 == 1:   # 홀수
                        odd = False
                # 해당 배열 초기화,
                arr[j][i] = []
                if m < 5:
                    pass        # 소멸해야됌
                else:
                    if even or odd:
                        for new_d in [0, 2, 4, 6]:
                            arr[j][i].append([m//5, v//cnt, new_d])
                    else:
                        for new_d in [1, 3, 5, 7]:
                            arr[j][i].append([m//5, v//cnt, new_d])

    return arr

# K 번 만큼 작업 수행해주기
for _ in range(K):
    graph = moving()

ans = 0
for i in range(N):
    for j in range(N):
        for info in graph[j][i]:
            ans += info[0]

print(ans)