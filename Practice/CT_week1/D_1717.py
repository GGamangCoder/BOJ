# 집합의 표현

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_lst = {}
for idx in range(n+1):
    set_lst[idx] = set()

for i in range(m):
    oper, a, b = map(int, input().split())
    # 무조건 작은게 a 라고 해보자.
    if a > b:
        a, b = b, a

    if oper == 0:
        if a == b:
            continue
        set_lst[a].add(b)
    else:
        if b in set_lst[a] or a == b:
            print('YES')
        else:
            print('NO')