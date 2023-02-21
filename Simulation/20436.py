# ZOAC3

keyboard_left = ['qwert', 'asdfg', 'zxcv']
keyboard_right = ['0yuiop', '0hjkl', 'bnm']     # 앞에 빈공간 b 때문에

SL, SR = input().split()
string = input()

# 첫 번째 왼손/오른손 위치
for line in range(len(keyboard_left)):
    if SL in keyboard_left[line]:
        lx, ly = keyboard_left[line].index(SL), line

for line in range(len(keyboard_right)):
    if SR in keyboard_right[line]:
        rx, ry = keyboard_right[line].index(SR), line

ans = 0
for s in string:
    # 자음 파트
    for line in range(len(keyboard_left)):
        if s in keyboard_left[line]:
            x, y = (keyboard_left[line].index(s), line)
            ans += abs(x - lx) + abs(y - ly) + 1
            lx, ly = x, y
            break
    # 모음 파트
    for line in range(len(keyboard_right)):
        if s in keyboard_right[line]:
            x, y = (keyboard_right[line].index(s), line)
            ans += abs(x - rx) + abs(y - ry) + 1
            rx, ry = x, y
            break

print(ans)