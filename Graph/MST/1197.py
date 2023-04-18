# 최소 스패닝 트리

import sys
input = sys.stdin.readline


V, E = map(int, input().split())
# 처음 부모 세팅 - 자기 자신
parent = [x for x in range(V+1)]
# 입력되어지는 간선들 종류
edge = [[0] for _ in range(E)]
for i in range(E):
    edge[i] = list(map(int, input().split()))

edge.sort(key=lambda x: x[2])

# 부모 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 부모 일치시키기
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

ans = 0
for start, end, val in edge:
    if find(start) != find(end):
        # 작은 거 기준으로 해주자
        if start > end:
            start, end = end, start
        union(start, end)
        ans += val

print(ans)