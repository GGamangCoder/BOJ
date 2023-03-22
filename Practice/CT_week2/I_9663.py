# N-Queen
# N * N 크기의 체스판 위에 퀸 N개
# Pypy3 로 해결

n = int(input())

# 첫 번째 행의 각 열에 대해 몇 번째 행에 존재하는지 나타냄
arr = [0] * n

cnt = 0     # 경우의 수(답)
# 여기서 x라는 것은 검사하는 열이라 하자
def dfs(x):       # 한 행을 기준으로 마지막 행까지 검사가 끝나는 경우 생각
    global cnt
    if x == n:      # n-1 까지 검사를 끝나고 나서 n 번째에 리턴
        cnt += 1
        return
    
    # 각 열(x)에서 말이 존재하는 위치의 행은?
    for row in range(n):
        arr[x] = row
        # 이전 열들에 대해 검사, 여기를 통과해야 다음 과정 가능한 거
        for i in range(x):
            if arr[i] == arr[x] or abs(x-i) == abs(arr[x]-arr[i]):
                break
        else:
            dfs(x+1)

dfs(0)
print(cnt)