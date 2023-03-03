# 직사각형
# 공통되는 영역이 있는지 여부 판별

def check():
    # 영역에서 벗어난 경우
    if rx1 < lx2 or ry1 < ly2 or rx2 < lx1 or ry2 < ly1:
        return 'd'
    # 위의 조건문 통과하면 어쨋든 안에 겹치는 부분이 있단겨
    # x좌표가 일치할 때,
    elif rx1 == lx2 or rx2 == lx1:
        # 만약 y좌표도 일치한다면
        if ry1 == ly2 or ry2 == ly1:
            return 'c'
        # y좌표 일치 안하면 선을 끼고 있는겨
        else:
            return 'b'
    if ry1 == ly2 or ry2 == ly1:
        return 'b'
    else:
        return 'a'

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = list(map(int, input().split()))
    print(check())