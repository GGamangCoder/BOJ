# 빙고 게임

bingo = [list(map(int, input().split())) for _ in range(5)]

bingo_row = list(map(list, zip(*bingo)))
bingo_cross = []

bingo_cross = [[] for _ in range(2)]
for i in range(5):
    bingo_cross[0].append(bingo[i][i])
    bingo_cross[1].append(bingo[i][4-i])

bingo_all = bingo + bingo_row + bingo_cross

mc_num = []
for i in range(5):
    mc_num += list(map(int, input().split()))

cnt = 0         # 게임 진행 횟수
for num in mc_num:
    cnt += 1
    bingo_cnt = 0       # 빙고 라인 수
    for j in range(12):
        if num in bingo_all[j]:
            bingo_all[j].remove(num)
        if bingo_all[j] == []:
            bingo_cnt += 1
    if bingo_cnt >= 3:
        break

print(cnt)
