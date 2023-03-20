# N-Queen
# N * N 크기의 체스판 위에 퀸 N개

# 행(혹은 열)의 갯수와 퀸의 갯수가 일치하므로 한 라인에서,
# 다음으로 대각선에서 겹치지 않도록 세팅한다.



n = int(input())

# graph = [0] * n       # 하나씩 보면..
graph = [[0] * n for _ in range(n)]

cnt = 0     # 경우의 수(답)
def dfs(x):       # 한 행을 기준으로 마지막 행까지 검사가 끝나는 경우 생각
    global cnt
    if x == n:
        cnt += 1
        return
    
    for i in range(n):
        flag = 0
        for j in range(n):
            if not graph[j][i]:
                pass