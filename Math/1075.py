N = int(input())
F = int(input())

num = N // 100 * 100
for i in range(100):
    if (num + i) % F == 0:
        break
if i < 10:
    print(str(0)+str(i))
else:
    print(i)