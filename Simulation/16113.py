# 시그널
# 다섯 줄씩 배열로 넣어주고, 각 라인을 판단하여 숫자 확인
# 참고로 0, 2~9는 하나당 3칸을 차지하고 1만 1칸을 차지한다.

N = int(input())
input_ = input()
leng = N // 5        # 구간, line 1~5
codes = [[] for _ in range(5)]
for i in range(5):
    codes[i] += input_[leng*i:leng*(i+1)]

# 90도 오른쪽으로 돌려서 세워줌
codes = list(zip(*codes))

# 돌린 상태를 위에서 부터 체크, 총 길이 leng만큼
# 3줄을 담아놔야되기 때문에 빈 리스트를 이용
ans = ''
lst = []
idx = 0     # 3회 반복하는지 임시 변수
print(codes)
for i in range(leng):
    temp = ''.join(codes[i])
    if temp == '.....':
        # 리스트 담겨있으면 그건 1일거야
        if lst:
            ans += '1'
            lst = []
            idx = 0
        continue
    # 새로 시작
    else:
        if idx == 0:
            if temp == '#####':
                lst += ['0', '6', '8']        # 1은 위에서 처리
                idx += 1
            elif temp == '#.###':
                lst += ['2']
                idx += 1
            elif temp == '#.#.#':
                lst += ['3']
                idx += 1
            elif temp == '###..':
                lst += ['4']
                idx += 1
            elif temp == '###.#':
                lst += ['5', '9']
                idx += 1
            elif temp == '#....':
                lst += ['7']
                idx += 1
        elif idx == 1:
            if len(lst) == 1:
                idx += 1
            elif temp == '#...#':
                lst = ['0']
                idx += 1
            else:       # 6, 8(0,6,8 in lst) / 5, 9 경우에 대해 스킵
                idx += 1
        else:       # 마지막(idx = 2)
            if len(lst) == 1 or temp == '#####':
                ans += lst[-1]          # 8, 9
            else:
                ans += lst[-2]          # 6, 5
            # 초기화
            idx = 0
            lst = []

if lst:
    ans += '1'
print(ans)