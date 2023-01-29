# 트리의 부모 찾기
# 2중 리스트

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]    # 1~N 맞춰주기 위해서
parent = [0] * (N+1)            # graph와 마찬가지, 숫자(int)

for _ in range(N-1):
    Point1, Point2 = map(int, input().split())
    graph[Point1].append(Point2)
    graph[Point2].append(Point1)

def bfs():     # point is node(노드)
    queue = deque([])
    queue.append(1)     # 루트 노드가 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)
    return parent


bfs()
for i in parent[2:]:
    print(i)