# 사이클 게임

# 완성 되었는지 판단, 완성되었다면 몇 번째에 완성됐는지 - 


import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
p = [i for i in range(n)]

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
    elif x > y:
        p[x] = y


res = 0
for i in range(1, m+1):
    x, y = map(int, input().split())
    if find(p[x]) == find(p[y]) and not res:
        res = i
    if res:
        continue
    union(x, y)
print(res)