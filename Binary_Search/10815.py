## 숫자 카드 문제 (10816 문제랑 동일)
## Binary Search

import sys

input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
checks = list(map(int, input().split()))

for check in checks:
    left, right = 0, N-1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] > check:
            right = mid -1
        elif cards[mid] < check:
            left = mid + 1
        else:               # 중간값이 곧 결과값
            flag = True
            break
    print(1 if flag else 0, end= ' ')