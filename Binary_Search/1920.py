# 수 찾기 문제
# 이분 탐색으로도 풀어볼 수 있는 문제
# 참고 - https://chancoding.tistory.com/43

import sys
input = sys.stdin.readline

# 자료형 이용
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)