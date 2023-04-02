# 부분합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = 10001
i = j = 0
s = lst[0]

while True:
    if s >= S:
        s -= lst[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        s += lst[j]

print(ans)