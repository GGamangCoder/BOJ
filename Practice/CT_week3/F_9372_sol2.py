# 상근이의 여행
# 신장 트리 풀이

import sys
input = sys.stdin.readline


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(M):
        input()

    print(N-1)