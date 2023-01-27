# 제로(10773)
# 여기서 그냥 input 값을 받을 경우에 비해서 readline의 런타임이 훨씬 빠르다는 것을 느끼게 해준 문제 

import sys
input = sys.stdin.readline

K = int(input())
num_list = []
for _ in range(1, K+1):
    n = int(input())
    if n != 0:
        num_list.append(n)
    else:
        num_list.pop()

print(sum(num_list))