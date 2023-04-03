# 피보나치 함수


import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]
def Fn(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Fn(N)
    print(zero[N], one[N])


# 두번째 풀이
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    zero = 1
    one = 0
    for i in range(N):
        zero, one = one, zero + one
    print(zero, one)
'''