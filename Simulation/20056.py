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


N, M, K = map(int, input().split())     # 크기, 갯수, 이동 횟수
graph = [[[] for _ in range(N)] for _ in range(N)]
print(graph)
# 방향
d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
for i in range(M):
    row, col, mass, vel, dir =\
        map(int, input().split())
    graph[row-1][col-1].append([mass, vel, dir])
print(graph)
######## 입력 끝
# K번의 이동 동작 수행
def moving():
    pass

# 합쳐졌다가 분해되는 것에 대한 계산
def seperate():
    pass

# 이동 후에 혹시 겹치는 부분 있는지 체크해주는 부분
