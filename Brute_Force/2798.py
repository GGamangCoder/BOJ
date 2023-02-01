# 블랙잭 문제

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            if result < total and total <= M:
                result = total
print(result)