# 빙고 게임
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
order = []
for _ in range(5):
    order += list(map(int, input().split()))


# 빙고 여부 확인
def check_bingo():
    res = 0
    for i in range(5):
        # 한 행
        if arr[i].count(0) == 5:
            res += 1
        # 한 열
        if list(zip(*arr))[i].count(0) == 5:
            res += 1
    # 대각선
    temp1 = temp2 = 0
    for i in range(5):
        if arr[i][i] == 0:
            temp1 += 1
        if arr[i][4-i] == 0:
            temp2 += 1
    if temp1 == 5:
        res += 1
    if temp2 == 5:
        res += 1
    if res == 3:
        return True
    else:
        return False

# 게임 진행
def game():
    cnt = 0
    while True:
        for i in order:
            for m in range(5):
                for n in range(5):
                    if arr[n][m] == i:
                        arr[n][m] = 0
                        cnt += 1
            if cnt >= 12 and check_bingo():
                return cnt

print(game())