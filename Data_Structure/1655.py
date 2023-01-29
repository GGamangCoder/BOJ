# 가운데를 말해요 - 힙 큐(Heap Queue)
# 개념 정리 필요!! - 자료구조(Priority Q, Heapq)

import sys
import heapq

N = int(sys.stdin.readline())
heap_left, heap_right = [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(heap_left) == len(heap_right):
        heapq.heappush(heap_left, -num)
    else:
        heapq.heappush(heap_right, num)
        
    if heap_right and heap_left[0] * -1 > heap_right[0]:
        max_value = heapq.heappop(heap_left) * -1
        min_value = heapq.heappop(heap_right)
        
        heapq.heappush(heap_left, min_value * -1)
        heapq.heappush(heap_right, max_value)

    print(heap_left[0] * -1)