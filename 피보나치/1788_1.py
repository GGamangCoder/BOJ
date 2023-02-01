n = int(input())
flag = 1
if n == 0:
    flag = 0
elif n < 0 and n % 2 != 0:
    flag = -1

Fn = [0, 1]
n = abs(n)
for _ in range(2, n + 1):
    Fn.append((Fn[-1]+Fn[-2])%1000000000)
    
print(flag)
print(Fn[n])