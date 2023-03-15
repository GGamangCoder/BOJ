# 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
p = [i for i in range(n+1)]

def find(x):
    if x == p[x]:
        return x

    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        p[y] = x
    else:
        p[x] = y

for _ in range(m):
    oper, x, y = map(int, input().split())
    if not oper:
        union(x, y)
    else:
        if find(x) == find(y):
            print('YES')
        else:
            print('NO')