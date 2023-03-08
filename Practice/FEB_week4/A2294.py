# 동전 2

# n가지의 동전 -> k원
# 결과는 가능한 최소 갯수, 불가능 -1
n, k = map(int, input().split())
val = set()
for _ in range(n):
    val.add(int(input()))
val = sorted(val)
dp = [0] * (k+1)        # 1부터 가치 k까지 빈 배열

# 1부터 차례대로 가치 창출