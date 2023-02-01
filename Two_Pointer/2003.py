N, M = map(int, input().split())
An = list(map(int, input().split()))

start, end = 0, 1
cnt = 0         # 경우의 수
temp = 0        # 합

while start <= N and end <= N:
    temp = sum(An[start:end])
    if temp == M:
        cnt += 1
        end += 1
    elif temp < M:
        end += 1
    else:   # temp > M:
        start += 1
print(cnt)