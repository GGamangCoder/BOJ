# 우유 도시

# 딸기 - 초코 - 바나나 - 딸기
# bfs 문제로 확장해 나가기를 생각했다가, 왼쪽과 위(그 이전)에 어떻게 영향 받을지를 고려

N = int(input())        # 배열 크기
graph = [list(map(int, input().split())) for _ in range(N)]
# 0행, 0열 패딩
# graph 랑 인덱스가 1씩 차이 나는 거 고려해주기
# 사먹은 우유(1, 2, 3, ...)를 기록하고, 현재까지 먹은 우유(0, 1, 2)를 최신화
drink_milk = 0
current_milk = -1       # 1, 1 은 0 부터 시작이므로
ans = [[[drink_milk, current_milk] for _ in range(N+1)] for _ in range(N+1)]

for j in range(1, N+1):
    for i in range(1, N+1):
        # 왼쪽, 오른쪽 우유 배열 / 누적 우유, 현재
        left, up = ans[j][i-1], ans[j-1][i]
        # 다음 맛 우유 먹을 수 있는지
        left_next = (graph[j-1][i-1] == (left[1]+1) % 3)
        up_next = (graph[j-1][i-1] == (up[1]+1) % 3)

        left_milk = left[0] + left_next
        up_milk = up[0] + up_next
        
        # 바뀔 결과 비교하여 증가하는 경우를 담기
        if left_milk > up_milk:
            ans[j][i][0] = left_milk
            # 값이 변화했으면 다음 먹을 우유 최신화
            if left_next:
                ans[j][i][1] = left[1] + 1
            # 그게 아니라면 우유 맛 변화없이 그대로
            else:
                ans[j][i][1] = left[1]

        # 위에서 영향받는 경우가 더 클 경우
        else:
            ans[j][i][0] = up_milk
            if up_next:
                ans[j][i][1] = up[1] + 1
            else:
                ans[j][i][1] = up[1]

# 싹 돌려서 마지막 결과의 누적 우유 출력
print(ans[N][N][0])