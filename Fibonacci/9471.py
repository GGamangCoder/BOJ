# 주기라는 것은 결국에 다시 반복되는 구간을 찾는 것.
# Fn 은 처음 시작이 0, 1, 1, 2, ... 이므로 2보다 큰 경우(즉 3이상의 경우)에 대해서는 나머지가 0, 1, 1, 2, .. 인 구간이 있다는 것!
# 다시금 이 구간을 찾아주면 된다.(이에 대한 증명은 Wall씨가 했으므로 ..)

##### 여기서 중요한 성질 하나(moduler 산술 성질) #####
# (a + b) % m = (a % m + b % m) % m   # -도 성립
# (a * b) %m = (a % m * b* m) % m
##### a + b = Fn[n], a = Fn[n-1], b = Fn[n-2] 로 이해할 수 있기 때문.

## pass 코드
import sys
input = sys.stdin.readline

P = int(input())

for _ in range(1, P+1):
    T = 1       # 주기
    mod1, mod2 = 1, 1
    N, M = map(int, input().split())

    while True:
        if mod1 % M == 0 and mod2 % M == 1:
            break

        T += 1
        mod1, mod2 = mod2, (mod1+mod2)%M
    
    print('{} {}'.format(N, T))


## 하기는 수정해야할 내용
import sys
input = sys.stdin.readline

P = int(input())

for test_case in range(1, P+1):
    Fn = [0, 1]
    T = 1       # 주기

    N, M = map(int, input().split())

    while True:
        if Fn[-2] % M == 0 and Fn[-1] % M == 1:
            break

        T += 1
        Fn.append((Fn[-2]+Fn[-1]) % M)

    print('{} {}'.format(N, T))
    
