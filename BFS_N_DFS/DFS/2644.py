import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
comp1, comp2 = map(int, input().split())
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

def dfs(node):
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = visited[node] + 1
            dfs(n)

dfs(comp1)
if not visited[comp2]:
    print(-1)
else:
    print(visited[comp2])