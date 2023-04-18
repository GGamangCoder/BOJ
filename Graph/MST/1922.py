# 네트워크 연결(골드 4)
# MST

import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

edge = [[0] for _ in range(M)]
for i in range(M):
    edge[i] = list(map(int, input().split()))
# 간선의 가중치 최소인 것 순으로 정렬
edge.sort(key=lambda x: x[2])

parent = [x for x in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

ans = 0
for s, e, v in edge:
    if find(s) != find(e):
        if s > e:
            s, e = e, s
        union(s, e)
        ans += v

print(ans)