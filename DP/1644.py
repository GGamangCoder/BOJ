# 소수의 연속합

from math import sqrt

n = int(input())
arr = [True] * (n+1)
arr[0] = False
arr[1] = False

# 에라토스테네스의 체 구현
def Prime_List(lst, num):
    prime = []
    for i in range(2, num+1):
        if lst[i]:
            prime.append(i)
            for j in range(2 * i, num+1, i):
                lst[j] = False
    return prime, lst

prime_num, arr = Prime_List(arr, n)
prime_num += [0]

s = e = 0
cnt = 0
res = prime_num[0]

# 투포인터 구현, 소수합 구하기
while e < len(prime_num)-1:
    if res == n:
        cnt += 1
        res -= prime_num[s]
        s += 1
        e += 1
        res += prime_num[e]
    elif res < n:
        e += 1
        res += prime_num[e]
    else:
        res -= prime_num[s]
        s += 1

print(cnt)