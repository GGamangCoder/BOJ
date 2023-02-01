# 검문 - 숫자 N개, M으로 나눌 때 나머지 같은 모든 M 출력

import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))
min_num = min(num_list)
ans = set()

for i in range(min_num, 1, -1):
    for j in range(N-1):
        if num_list[j] % i != num_list[j+1] % i:
            break
        elif j == N-2:
            ans.add(i)
ans = sorted(list(ans))
for a in ans:
    print(a, end=' ')