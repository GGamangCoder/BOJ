# 경비원

w, h = map(int, input().split())
N = int(input())
arr =[]             # 위치 이동량 담을 리스트
s = w+w+h+h         # 둘레
for _ in range(N+1):
    rot, point = map(int, input().split())
    # 왼쪽 상단을 기준으로 얼마만큼 이동하는지
    if rot == 1:
        arr.append(point)
    elif rot == 2:
        arr.append(s-h - point)
    elif rot == 3:
        arr.append(s - point)
    elif rot == 4:
        arr.append(w + point)
    # 마지막이 동근이 위치
ans = 0
for i in range(N):
    # 거리 차이
    ds = abs(arr[i] - arr[-1])
    # 단순 거리 차이와 반대 방향 거리 차이 중에 최솟값
    ans += min(ds, s-ds)
print(ans)