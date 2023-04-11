# 숫자 정사각형 - 그리디

def find_squre(s):
    for i in range(N-s+1):          # 행
        for j in range(M-s+1):      # 열
            if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return True

    return False


N, M = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(N)]

size = min(N,M)

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k):
        print(k**2)
        break