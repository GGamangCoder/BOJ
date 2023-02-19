# 빙고 게임
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
order = []
for _ in range(5):
    order.extend(list(map(int, input().split())))

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
    temp = 0
    for i in range(5):
        if arr[i][i] == 0:
            temp += 1
    if temp == 5:
        res += 1
    temp = 0
    for i in range(5):
        if arr[i][4-i] == 0:
            temp += 1
    if temp == 5:
        res += 1
    if res == 3:
        return True

# 게임 진행
def game():
    cnt = 0
    for i in order:
        for m in range(5):
            for n in range(5):
                if arr[n][m] == i:
                    arr[n][m] = 0
                    cnt += 1
        if cnt >= 12 and check_bingo():
            return cnt

print(game())