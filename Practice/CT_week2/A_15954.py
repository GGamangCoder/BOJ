# 카카오 - 인형들 배치 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
temp = sum(lst[:K]) / K
ans = 0
for i in range(K):
    ans += (lst[i] - temp) ** 2
ans = (ans / K)**0.5

for i in range(1, N-K+1):
    temp = lst[i:i+K]       # 임시 리스트
    mean = sum(temp)/K
    new_sum = 0
    for i in temp:
        new_sum += (mean-i)**2
    new_sum = (new_sum / K) ** 0.5
    
    if new_sum <= ans:
        ans = new_sum
print(ans)


# import sys

# N, K = map(int, input().split())
# prefered = list(map(int, input().split()))

# min_std = float('inf')

# while(K != (N + 1)):
#     stride = 1
#     full_range = ((N - K) // stride) + 1
    
#     for i in range(full_range):
#         do_list = prefered[i:(i + K)]
#         mean = sum(do_list) / K
#         var = sum([(x - mean) ** 2 for x in do_list]) / K
#         std = var ** 0.5
#         if(min_std >= std):
#             min_std = std
#     K += 1
# sys.stdout.write(str(min_std))