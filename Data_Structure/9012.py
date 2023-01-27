# 괄호 문제

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    str = input().rstrip()
    res = 'YES'
    left = 0
    for i in str:
        if i == '(':
            left += 1
        elif i == ')':
            left -= 1

        if left < 0:
            res = 'NO'
            break
    if left > 0:
        res = 'NO'
    print(res)