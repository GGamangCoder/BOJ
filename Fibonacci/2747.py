# 10870 도 동일

import sys
input = sys.stdin.readline().rstrip

n = int(input())

Fn = [0, 1]
for i in range(2, n+1):
    Fn.append(Fn[-1]+Fn[-2])

print(Fn[n])
