# 창고 다각형

N = int(input())
arr = [0] * 1001
left = 1000         # 반복 구간 왼쪽, 최댓값을 초기값
right = 0           # 반복 구간 오른쪽, 초기화
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    left = min(left, L)         # 생략 가능
    right = max(right, L)
maxhigh = max(arr)         # 최대 높이
idx = arr.index(maxhigh)

res = 0             # 결과값 
high = 0            # 초기화
# 왼쪽 사이드
for i in range(left, idx):
    if arr[i] > high:
        high = arr[i]
    res += high

high = 0            # 초기화
res += maxhigh       # 최고 높이
for i in range(right, idx, -1):
    if arr[i] > high:
        high = arr[i]
    res += high


print(res)