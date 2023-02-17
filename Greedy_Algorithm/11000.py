# 강의실 배정 - 그리디
# 힙에는 가장 작은 원소로부터 정렬됨

import heapq

N = int(input())            # 수업 갯수
lecture_list = [0] * N      # 수업 타임 담을 공간
heap = []
for i in range(N):
    lecture_list[i] = list(map(int, input().split()))
# 시작 시간 빠른 순으로 정렬하여 뒤로 붙이기
lecture_list.sort()
heapq.heappush(heap, lecture_list[0][1])
for i in range(1, N):
    # 끝날 시간보다 빠르면 일단 담아놓기
    if lecture_list[i][0] < heap[0]:
        heapq.heappush(heap, lecture_list[i][1])
    else:
        heapq.heappop(heap)     # 가장 빠른 종료 강의
        heapq.heappush(heap, lecture_list[i][1])

print(len(heap))
