# AC, 새로운 언어 문제

from collections import deque

T = int(input())

for _ in range(1, T+1):
    p = input()
    n = int(input())
    R = 0       # R 횟수
    flag = False
    Numlist = deque(input()[1:-1].split(','))
    if n == 0:
        Numlist = deque()

    for str in p:
        if str == 'R':
            R += 1
        elif str == 'D':
            if len(Numlist) == 0:
                flag = True
                break
            else:
                if R % 2 == 0:
                    Numlist.popleft()
                else:
                    Numlist.pop()   

    if flag == True:
        print('error')
    else:
        if R % 2 == 0:
            print("[" + ",".join(Numlist) + "]")
        else:
            Numlist.reverse()
            print("[" + ",".join(Numlist) + "]")