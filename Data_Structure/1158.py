# 요세푸스 문제

from collections import deque

N, K = map(int, input().split())

def josephus(n, k):
    queue = deque([i for i in range(1, n+1)])
    res = []
    while len(queue) > 0:
        queue.rotate(-k+1)
        num = queue.popleft()
        res.append(str(num))
    return res

ans = josephus(N, K)
print('<', ', '.join(ans[:]), '>', sep='')