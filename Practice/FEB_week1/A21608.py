N = int(input())
arr = [[0]*N for _ in range(N)]
like = []

for _ in range(N**2):
    A = list(map(int, input().split()))
    like.append(A)