# 카카오 - 상금 헌터

def coin_1st(a):
    gold = 0
    if a == 0:
        return 0
    if a == 1:
        gold = 5000000
    elif a <= 3:
        gold = 3000000
    elif a <= 6:
        gold = 2000000
    elif a <= 10:
        gold = 500000
    elif a <= 15:
        gold = 300000
    elif a <= 21:
        gold = 100000
    return gold

def coin_2nd(a):
    gold = 0
    if a == 0:
        return 0
    if a == 1:
        gold = 5120000
    elif a <= 3:
        gold = 2560000
    elif a <= 7:
        gold = 1280000
    elif a <= 15:
        gold = 640000
    elif a <= 31:
        gold = 320000
    return gold

def sum_coin(a, b):
    return a+b


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(sum_coin(coin_1st(a), coin_2nd(b)))