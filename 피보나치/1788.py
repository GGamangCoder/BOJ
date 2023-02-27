n = int(input())
flag = 0        # n이 0일 때
if n > 0:
    flag = 1
elif n < 0:
    flag = -1

Fn = [0, 1]
n = abs(n)
for _ in range(2, n + 1):
    Fn.append((Fn[-1]+Fn[-2])%1000000000)

if flag == -1:      # 음수일 때,
    if n % 2 != 0:
        flag = -flag

print(flag)
print(Fn[n])