# 트리의 지름

import sys
input = sys.stdin.readline

def dfs(start, cur):
    for s, c in graph[start]:
        if v[s] == -1:      # 미방문
            v[s] = cur + c
            dfs(s, cur + c)


n = int(input())
# 노드 연결 상태 - 트리
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, val = map(int, input().split())
    graph[p].append([c, val])
    graph[c].append([p, val])
    
v = [-1] * (n + 1)
v[1] = 0        # 시작 노드 초기화

dfs(1, 0)
temp = v.index(max(v))

v = [-1] * (n + 1)
v[temp] = 0
dfs(temp, 0)

print(max(v))