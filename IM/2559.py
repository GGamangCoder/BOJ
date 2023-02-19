# 수열(실버3)

N, K = map(int, input().split())
T = list(map(int, input().split()))     # type list

ans = res = sum(T[:K])
for i in range(1, N + 1 - K):
    res = res - T[i-1] + T[i+K-1]
    if ans < res:
        ans = res
print(ans)