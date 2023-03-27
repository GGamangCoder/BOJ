# 상근이의 여행
# DFS 풀이

import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    visited[idx] = 1

    for i in graph[idx]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)
    
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(dfs(1, 0))