# 너 봄에는 캡사이신이 맛있단다 (골드 2)
<<<<<<< HEAD
# 스코빌 지수 - 주헌고통지수

# 1,000,000,007 로 나눈 나머지(소수임)
# 모든 경우의 합 = 각 경우의 최댓값의 합 - 최솟값의 합
# 근데 각 경우는 만들 수 있는 조합 수의 곱
# 출처 - https://0902.tistory.com/60
# 출처2 - 


import sys
input = sys.stdin.readline

mod = 1000000007


def sort(a, b):
    pass


n = int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(n):
    
=======
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
>>>>>>> aa15c4d7ceba6fae5e25769bc30ff3b4ef3ca220
