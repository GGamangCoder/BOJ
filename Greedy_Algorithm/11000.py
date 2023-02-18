# 강의실 배정 - 그리디
# 힙에는 가장 작은 원소로부터 정렬됨

import heapq

N = int(input())            # 수업 갯수
heap = []
lecture_list = [list(map(int, input().split())) for _ in range(N)]
lecture_list.sort(key = lambda x: x[0])
heapq.heappush(heap, lecture_list[0][1])
for i in range(1, N):
    # 끝날 시간보다 빠르면 일단 담아놓기
    if lecture_list[i][0] < heap[0]:
        heapq.heappush(heap, lecture_list[i][1])
    else:
        heapq.heappop(heap)     # 가장 빠른 종료 강의
        heapq.heappush(heap, lecture_list[i][1])

print(len(heap))
