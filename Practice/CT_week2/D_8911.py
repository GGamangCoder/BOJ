# 거북이 

# F: 한 눈금 앞으로, B: 한 눈금 뒤로, L: 왼쪽으로 회전, R: 오른쪽 회전

import sys
input = sys.stdin.readline


# 영역을 계산해주는 함수
def solve(cmd):
    direction = lx = rx = ty = by = 0       # 현재 방향, 왼/오, 위/아래
    x = y = 0
    # 명령 받는대로
    for s in cmd:
        if s == 'L':
            direction -= 1
        elif s == 'R':
            direction += 1

        # 현재 방향대로 전진 혹은 후진
        elif s == 'F':
            pass
        elif s == 'B':
            pass



T = int(input())
for tc in range(1, T+1):
    command = input()
    print(solve(command))
