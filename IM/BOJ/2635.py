# 수 이어가기

# 1. 양수
# 2. 양의 정수 중 하나 선택
# 3. 3 = 1 - 2, 4 = 2 - 3, ...
# 4. 음의 정수 나오면 스탑


n = int(input())
i = n//2
res = [n, i]
while i <= n:
    dp = [n, i]
    while True:
        if dp[-2] - dp[-1] >= 0:
            dp.append(dp[-2] - dp[-1])
        else:
            break
    
    if len(res) < len(dp):
        res = dp

    i += 1

print(len(res))
print(*res)