# 색종이 넓이

N = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(N):
    x, y = map(int, input().split())
    for m in range(x, x+10):
        for n in range(y, y+10):
            arr[n][m] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[j][i] == 1:
            cnt += 1
print(cnt)