# 랜선 자르기

K, N = map(int, input().split())
# K <= 10,000 & N <= 1,000,000

lst = [0] * K
ans = 0
for i in range(K):
    temp = int(input())
    lst[i] = temp
    ans += temp

ans //= N       # 완전 최댓값
min_rg = max(lst) // N

for i in range(ans, min_rg, -1):
    cnt = 0
    for j in range(K):
        cnt += lst[j] // i
    if cnt >= N:
        ans = i
        break

print(ans)