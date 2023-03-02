# 마법사 상어와 블리자드

# 문제
# 방향(di) 1, 2, 3, 4 = 위 아래 왼 오 / 거리(si)
# 1. 방향대로 거리만큼 터뜨려       - 얼음 파편
# 2. 앞으로 구슬을 땡겨줘
# 3. 연속된 숫자 4개 이상은 다 터뜨려(폭발)
# 4. 그리고 2, 3 반복
# 5. 끝나면 연속한 구슬은 하나의 그룹이라고 두고 A(개수), B(구슬 번호)
    # 만약 구슬이 사이즈보다 크면 사라짐
# 결과는 i * (폭발 i 갯수)

# 블리자드 M번 시행
# 배열 선언 후에
# 마법 시행 방법 안내

di = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cnt1 = cnt2 = cnt3 = 0

# N: 사이즈, M: 시전 횟수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = []
s = []
for _ in range(M):
    temp = input().split()
    d.append(temp[0])
    s.append(temp[1])

def first_boom(d, s):   # 방향과 거리
    pass

def second_boom():
    pass