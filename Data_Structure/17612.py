# 쇼핑몰

import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 1             # 카운터 번호
waiting = []
finish = []
for i in range(n):
    # i번째 고객의 id(p) / 구입한 물건 수 w
    p, w = map(int, input().split())



# 빠져나가는 순서대로 회원번호 r1, r2, r3, ... rn
