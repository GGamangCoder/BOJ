# 징검다리 건너기(large)

# 돌의 갯수
N = int(input())
# N개의 돌 리스트
stones = list(map(int, input().split()))
# 경로를 누적하여 담을 리스트
dp = [0] * N
# 오른쪽 이동, i->j; (j-i) * (1 + abs(stones[j]-stones[i]))

for i in range(N):
    pass

