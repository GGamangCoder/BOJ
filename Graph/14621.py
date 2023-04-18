# 나만 안되는 연애
# MST
# 출처 - https://velog.io/@030831/%EB%B0%B1%EC%A4%80-14621-%EB%82%98%EB%A7%8C-%EC%95%88%EB%90%98%EB%8A%94-%EC%97%B0%EC%95%A0-Python
# 출처 - https://kimmeh1.tistory.com/394 


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 각 지점에 대해서 스스로 부모 노드
parent = [x for x in range(n+1)]        # 0, 1~n
v = [True] + [False]*n                  # 방문에 대한,
node = [0] + list(input().split())
# 간선에 대한 정보, [시작, 끝, 크기]
edge = [[0] for _ in range(m)]
for i in range(m):
    edge[i] = list(map(int, input().split()))

# 간선의 크기에 따라 정렬
edge.sort(key=lambda x: x[2])
ans = 0
cnt = 0

##############################################
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# y 보다 x 가 더 크다고 하자.
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
##############################################


for start, end, val in edge:
    # 부모 노드가 다르고, 학교 성별이 다를 때만
    if find(start) != find(end) and node[start] != node[end]:
        union(start, end)
        ans += val
        v[start] = True
        v[end] = True

if False in v:
    ans = -1

print(ans)