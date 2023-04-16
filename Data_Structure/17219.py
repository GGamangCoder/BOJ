# 비밀번호 찾기
# 자료구조, 해쉬와 맵

import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
sites = defaultdict()
for _ in range(n):
    site, pwd = input().split()
    sites[site] = pwd

for _ in range(m):
    print(sites[input().rstrip()])