# 우유 축제
# next probelm recommend) boj #14722

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
milk = 0
for i in range(len(arr)):
    if arr[i] == milk % 3:
        cnt += 1
        milk += 1

print(cnt)