# 연결 요소의 갯수
# 2중 리스트

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]    # 1~N 맞춰주기 위해서
visited = [False] * (N+1)           # graph와 마찬가지

for _ in range(M):
    Point1, Point2 = map(int, input().split())
    graph[Point1].append(Point2)
    graph[Point2].append(Point1)

def bfs(point):     # point is node(노드)
    queue = deque([point])
    visited[point] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:       # graph 연결된 노드들에 대해서
            if not visited[i]:      # 해당 노드 방문 한 적 없다면,
                visited[i] = True   # 방문 추가
                queue.append(i)     # 그 노드에 대한 반복

cnt = 0
for i in range(1, N+1):     # 1 ~ N 번 노드 체크
    if not visited[i]:      # 방문한 적 없는 노드에 대해
        if not graph[i]:    # 연결된 그래프 없다면 추가(단일 노드)
            cnt += 1
            visited[i] = True
        else:           # 방문한 적은 없는데, 연결된 점 있는 경우
            cnt += 1
            bfs(i)

print(cnt)