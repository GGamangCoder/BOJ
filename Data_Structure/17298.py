# 오큰수
# 오른쪽에 있는 가장 큰 수 중 가장 가까운 수

from collections import deque

N = int(input())
A = list(map(int, input().split()))
big = [-1] * N
stack = deque()

for i in range(N):
    while stack and stack[-1][0] < A[i]:
        temp, idx = stack.pop()
        big[idx] = A[i]
    # 인덱스와 해당 값을 입력
    stack.append((A[i], i))

print(*big)