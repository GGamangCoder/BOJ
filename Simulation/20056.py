# 마법사 상어와 파이어볼
# 어른 상어 -> 마법사 상어

N * N 격자에, 파이어볼 M 개
i번 위치 - (ri, ci), 질량 mi, 방향 di, 속력, si 
모든 파이어볼 방향과 속력대로 이동(한칸에 여러개 가능)
같은 칸의 파이어볼 하나로 합쳐짐 - 4개로 나누어짐

1. 질량 - 합질량/5
2. 속력 - 속력합/갯수
3. 방향 - 모두 홀수거나 짝수면 0, 2, 4, 6 / 아니면 1, 3, 5, 7
* 질량이 0이면 소멸

K 번 이동 -> ans; 남은 질량 합


N, M, K = map(int, input().split())             # 크기, 갯수, 
rows = [0] * M          # 행
cols = [0] * M          # 열
mass = [0] * M          # 질량
vel = [0] * M           # 속력
dir = [0] * M           # 방향 -> d
# 방향
d = [(0, -1), (1, -1), (1, 0), (1, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
for i in range(M):
    rows[i], cols[i], mass[i], vel[i], dir[i] =\
        map(int, input().split())
######## 입력 끝

