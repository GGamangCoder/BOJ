# 반복 수열
# 수학, 구현

dp = []

# str
A, P = input().split()
dp = [A]

def sum(num):
    ans = 0
    for i in num:
        ans += int(i)**int(P)
    return str(ans)

res = 0
idx = 0
while True:
    dp_next = sum(dp[idx])
    if dp_next in dp:
        res = dp.index(dp_next)
        break
    else:
        dp.append(dp_next)
        idx += 1

print(res)