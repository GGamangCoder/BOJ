# 행성 연결(골드 4)
# 그래프 이론 - MST

import sys
input = sys.stdin.readline


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 여기서는 0 ~ N 까지 이므로
parent = [i for i in range(N)]
# 간선 갯수 - 이따가 생략해보자
edge_cnt = N * (N-1) // 2
edge = [0] * edge_cnt

cnt = 0
for j in range(N):
    for i in range(j):
        edge[cnt] = (graph[j][i], i, j)
        cnt += 1
edge.sort()


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = x

ans = 0
for v, s, e in edge:
    if find(s) != find(e):
        if s > e:
            s, e = e, s
        union(s, e)
        ans += v

print(ans)