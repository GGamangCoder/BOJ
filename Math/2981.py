# 검문(백준 2981) - 숫자 N개, M으로 나눌 때 나머지 같은 모든 M 출력

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
min_num = min(num_list)
ans = deque()
ans2 = deque()

for i in range(min_num, 1, -1):
    flag = False
    for j in range(N-1):
        if num_list[j] % i != num_list[j+1] % i:
            flag = True
            break
    if flag == False:
        ans.appendleft(i)

# 나머지가 min_num인 경우
num_list.remove(min_num)
min_num2 = min(num_list)        # 두 번째 작은 수
for i in range(min_num2 - min_num, min_num-1, -1):
    flag = False
    # 시간을 조금이라도 줄여주고자
    if min_num2 % i != min_num:
        continue
    for j in range(N-1):
        if num_list[j] % i != min_num:
            flag = True
            break
    if flag == False:
        ans2.appendleft(i)

print(*ans, *ans2)
