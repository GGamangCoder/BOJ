# 최대 힙
# 음수로 주면 최댓값이 곧 최솟값이 되게 하여,
# 힙을 최대힙처럼 구현할 수 있다.

import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1)*x)