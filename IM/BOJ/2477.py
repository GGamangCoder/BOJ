# 참외밭 넓이

# 단위 넓이당 갯수
K = int(input())
width = height = 0
w_idx = h_idx = 0
# 방향 지정
arr = [list(map(int, input().split())) for _ in range(6)]
for i in range(6):
    # 방향 같은 것끼리 생각, 가장 긴 경우 체크
    if (arr[i][0]-1) // 2 == 0:     # 왼 오
        if width < arr[i][1]:
            width = arr[i][1]
            w_idx = i
    else:                           # 위 아래
        if height < arr[i][1]:
            height = arr[i][1]
            h_idx = i
# 가장 긴 변의 양 옆 높이 차
# 가장 긴 높이 양 옆 길이 차
subspace = abs(arr[(w_idx+1)%6][1] - arr[(w_idx-1)%6][1]) *\
    abs(arr[(h_idx+1)%6][1] - arr[(h_idx-1)%6][1])
print(K*(width*height - subspace))