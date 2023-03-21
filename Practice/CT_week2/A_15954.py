# 카카오 - 인형들 배치 문제
# 시간 초과로 인해 pypy3 로 해결

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
temp = sum(lst[:K]) / K
ans = 0
for i in range(K):
    ans += (lst[i] - temp) ** 2
ans = (ans / K)**0.5

while K != N+1:
    new_sum = 0
    for i in range(N-K+1):
        if new_sum == 0:
            temp = lst[i:i+K]
            mean = sum(temp) / K
            for i in temp:
                new_sum += (mean - i) ** 2
            new_sum = (new_sum / K) ** 0.5
        if new_sum <= ans:
            ans = new_sum
    K += 1
print(ans)
