# 피보나치 수의 확장
# 문제를 제대로 안 읽어 런타임 에러 ,, 다시 해서 극복
# 왜 위의 코드가 런타임 에러를 띄웠는지 나중에 체크해보자

###### Fn 이용
import sys
input = sys.stdin.readline().rstrip

n = int(input())
dic = {0:0, 1:1}
Fn_case = 1

if n == 0:
    Fn_case = 0
elif n < 0 and n %2 == 0:
    Fn_case = -1

def Fn(n):
    if n in dic:
        return dic[n]
    
    if n >= 2:
        dic[n] = (dic[n-2]+dic[n-1]) % 1000000000
        return dic[n]
    else:       # n < 0
        dic[n] = (dic[n+2]-dic[n+1]) % 1000000000
        return dic[n]

print('{}'.format(Fn_case))
print('{}'.format(abs(Fn(n))))

###### Pass code

