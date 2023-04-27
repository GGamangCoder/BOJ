# 너 봄에는 캡사이신이 맛있단다 (골드 2)
# 수학, 분할정복


import sys
MOD = 1000000007

# a는 밑, b는 지수
# 지수가 0, 1일 때를 구분하고 지수(b)가 짝수일 때와 홀수일 때를 구분한다
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a

    half = pow(a, b//2)
    # 반으로 나누어 떨어지지 않으면(홀수) a를 한 번 더 곱해준다.
    return half * half % MOD if b % 2 == 0 else half * half * a % MOD


N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0
 
for i in range(N):
    answer += arr[i] * (pow(2, i) - pow(2, N - i - 1))

print(answer % MOD)