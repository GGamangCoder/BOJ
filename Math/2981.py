# 검문 - 숫자 N개, M으로 나눌 때 나머지 같은 모든 M 출력

import sys
input = int(sys.stdin.readline())

def gcd(m,n):       # 최대 공약수
    while n != 0:
        t = m % n
        (m, n) = (n, t)
    return abs(m)

N = input
list = []
if N != 1:
    list.append(input)


#################### 미완