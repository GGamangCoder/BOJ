# 숨바꼭질 3
# 다익스트라(Dijkstra)


import sys
from heapq import heappop, heappush
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
maxVal = 100001             # 최댓값, 상수
dist = [maxVal] * 100001       # 거리

def dijkstra(n, k):
    dist[n] = 0
    # q 에는 (걸린 시간, 현재 위치)
    q = []
    heappush(q, (0, N))
    while q:
        time, pos = heappop(q)
        # 만약 도착했으면 스톱
        if pos == k:
            break
        for next in [(1, pos+1), (1, pos-1), (0, 2*pos)]:
            # 영역 내에 있고 방문 여부 체크
            if 0 <= next[1] < 100001 and dist[next[1]] > time + next[0]:
                dist[next[1]] = time + next[0]
                heappush(q, (dist[next[1]], next[1]))
    print(dist[k])

dijkstra(N, K)