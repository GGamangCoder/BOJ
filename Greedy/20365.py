# 블로그2

N = int(input())        # 배열 크기
Q = input()             # 문제 배열
state = Q[0]
change = 0
for i in range(1, N):
    if Q[i] == state:
        continue
    else:
        change += 1
        state = Q[i]
print((change+1)//2 +1)