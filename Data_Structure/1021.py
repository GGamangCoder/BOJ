# 회전하는 큐

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
number = deque([i for i in range(1, N+1)])
pos_list = deque(map(int, sys.stdin.readline().split()))

cnt = 0
for n in pos_list:
    while True:
        if n == number[0]:
            number.popleft()
            break
        else:
            if number.index(n) < len(number)/2:
                while n != number[0]:
                    number.rotate(-1)
                    cnt += 1
            else:
                while n != number[0]:
                    number.rotate()
                    cnt += 1

print(cnt)