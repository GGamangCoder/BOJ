# 2747 과는 다르게 재귀함수를 이용하여 짠 코드
# 재귀 함수는 함수 내에서 자기 자신을 계속해서 호출한다는 특징이 있다.
# 탈출 조건을 고려하기에 까다로우며 과도하게 스택 메모리를 이용하여 스택 오버플로우 에러가 생기는 경우가 종종 있다.
# 즉, 피보나치 수의 경우 시간 복잡도는 대략 O(2^n) 정도가 된다.
# 따라서 메모이제이션(Memoization)을 사용해야 한다.


import sys
input = sys.stdin.readline().rstrip

n = int(input())

def Fn(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return Fn(n-1) + Fn(n-2)
  
print(Fn(n))
