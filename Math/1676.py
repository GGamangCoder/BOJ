n = int(input())

idx = 1
ans = 0
while idx <= n:
    idx *= 5
    ans += n // idx

print(ans)