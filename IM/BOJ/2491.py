# 수열
N = int(input())        # == len(lst)
lst = list(map(int, input().split()))

# 연속되는 것을 누적하고, 조건을 만족하지 않을 경우 없애버림
# 그 자체로 한 개이므로 1로 초기화된 두 가지 dp 설정
dp_up = [1]*N       # 오름차순
dp_down = [1]*N     # 내림차순
for i in range(1, N):
    if lst[i-1] <= lst[i]:
        dp_up[i] = dp_up[i-1] + 1
    if lst[i-1] >= lst[i]:
        dp_down[i] = dp_down[i-1] + 1

# 각각의 최댓값을 구해 두 개 중 최댓값
print(max(max(dp_up), max(dp_down)))