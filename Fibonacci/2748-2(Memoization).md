참고: [백준 블로그 - 피보나치 수를 구하는 여러가지 방법 中](https://www.acmicpc.net/blog/view/28) 

선행 문제 - [2748(재귀함수)](https://github.com/GGamangCoder/BOJ/blob/main/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98/2748(%EC%9E%AC%EA%B7%80).py)  

재귀 함수의 문제를 해결하기 위해 동적 계획법(Dynamic Programming, DP)에서 활용되는 메모이제이션(Memoization)을 사용한다.
이 경우는 대략 O(n)의 시간복잡도를 갖는다.

```py
import sys
input = sys.stdin.readline().rstrip

n = int(input())
dic = {}

def Fn(n):
  if n in dic:
    return dic[n]
  
  if n == 0:
    dic[0] = 0
    return 0
  elif n == 1:
    dic[1] = 1
    return 1
  else:
    dic[n] = Fn(n-1)+Fn(n-2)
    return dic[n]
  
print(Fn(n))
```  

Fn(0)과 Fn(1)은 미리 값을 지정해주는 것이 내 스타일이다.  
```py
import sys
input = sys.stdin.readline().rstrip

n = int(input())
dic = {0:0, 1:1}

def Fn(n):
  if n in dic:
    return dic[n]
  
  dic[n] = Fn(n-1)+Fn(n-2)
  return dic[n]
  
print(Fn(n))
```

