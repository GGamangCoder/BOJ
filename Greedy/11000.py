# 강의실 배정

import heapq
import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()

cnt = 0
lab = []
for t in time:
    if not lab:
        heapq.heappush(lab, t[1])
        continue
    # 시작 시간
    if lab[0] <= t[0]:
        # 종료해서 처리해주기
        heapq.heappop(lab)
    # 시작 시간은 계속 넣기
    heapq.heappush(lab, t[1])

print(len(lab))