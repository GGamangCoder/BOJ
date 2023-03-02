# 줄어드는 수
# dfs(Back Tracking)

N = int(input())            # N <= 1000000

res = set()
num = []
def dfs():
    if num:
        res.add(int(''.join(map(str, num))))
    for i in range(10):
        if not num or num[-1] > i:
            num.append(i)
            dfs()
            num.pop()

try:
    dfs()
    res = sorted(list(res))
    print(res[N-1])
except:
    print(-1)