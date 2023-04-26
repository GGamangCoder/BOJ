# 너 봄에는 캡사이신이 맛있단다 (골드 2)
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
    