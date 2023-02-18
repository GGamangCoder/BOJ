# 주사위 쌓기

N = int(input())
dice = [0] * N
for i in range(N):
    temp = list(map(int, input().split()))
    # 주사위 짝 맞춰주기
    dice[i] = [temp[0], temp[5], temp[1], temp[3], temp[2], temp[4]]
# 주사위 쌓아주기 - 위 아래 제거
res = 0
for i in range(1, 7):   # 1~6 까지의 수
    num = i
    dice_sum = 0
    for j in range(N):  # 주사위 갯수
        print(num, end=':')
        if num == dice[j][0]:
            num = dice[j][1]
            dice_sum += max(dice[j][2:])
            print(dice[j][2:], end=' ')
        elif num == dice[j][1]:
            num = dice[j][0]
            dice_sum += max(dice[j][2:])
            print(dice[j][2:], end=' ')
        elif num == dice[j][2]:
            num = dice[j][3]
            dice_sum += max(max(dice[j][:2], dice[j][4:]))
            print(dice[j][:2], dice[j][4:], end=' ')
        elif num == dice[j][3]:
            num = dice[j][2]
            dice_sum += max(max(dice[j][:2], dice[j][4:]))
            print(dice[j][:2], dice[j][4:], end=' ')
        elif num == dice[j][4]:
            num = dice[j][5]
            dice_sum += max(dice[j][:4])
            print(dice[j][:4], end=' ')
        elif num == dice[j][5]:
            num = dice[j][4]
            dice_sum += max(dice[j][:4])
            print(dice[j][:4], end=' ')
    print()
    res = max(res, dice_sum)

print(res)