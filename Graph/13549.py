# 숨바꼭질3
# 0-1 bfs, Dijkstra
# 참고 - https://pottatt0.tistory.com/entry/%EB%B0%B1%EC%A4%80-13549-python-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-3 
# 실제 풀이 - https://donghak-dev.tistory.com/85 

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
v = [0] * 100001       # 0 ~ 10만

def bfs(n, k):
    q = deque([n])
    
    while q:
        node = q.popleft()
        if node == k:
            return v[node]

        for next_node in (node+1, node-1, node*2):
            if 0 <= next_node < 100001:
                if not v[next_node]:
                    # 앞으로 두고 계속 진행, 가중치 0
                    if next_node == node * 2 and next_node != 0:
                        v[next_node] = v[node]
                        q.appendleft(next_node)
                    # +1, -1 일 경우 가중치 1
                    else:
                        v[next_node] = v[node] + 1
                        q.append(next_node)

print(bfs(N, K))