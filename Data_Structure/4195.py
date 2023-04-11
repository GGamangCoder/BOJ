# 친구 네트워크

import sys
input = sys.stdin.readline

# 루트가 다른 경우 일치 시켜줌
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        network[x] += network[y]

# 부모 노드 찾아주기
# 요 놈을 어떻게 하느냐에 따라 결과가 다르게 나왔음.
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]        # == parent[x]


T = int(input())
for tc in range(T):
    E = int(input())        # 간선 수
    parent = dict()         # 친구 관계
    network = dict()        # 네트워크 상태
    # 친구 관계를 통해서는 union-find 해주고 network는 누적시켜주자.
    for _ in range(E):
        x, y = input().split()

        # 최초 독립적인 경우,
        if x not in parent:
            parent[x] = x
            network[x] = 1
        if y not in parent:
            parent[y] = y
            network[y] = 1
        
        union(x, y)
        print(network[find(x)])