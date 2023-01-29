# 나무 자르기
# 149776 KB	 4256 ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Woods = list(map(int, input().split()))

left, right= 1, max(Woods)
while left <= right:
    mid = (left + right) // 2
    res = 0         # 잘린 나무 길이 합
    for wood in Woods:
        if wood > mid:
            res += wood - mid
    #res = sum(Woods[mid:]) - Woods[mid] * len(Woods[mid:])
    if res < M:             # case 1, 오른쪽 땡길 때
        right = mid - 1
    else:        #(res >= M)
        left = mid + 1
print(right)


##### 두 번째 풀이 - 숏코딩(sait2000 님 풀이 발췌)
from bisect import*
def bin_trees(n, m, a):
    b=[0];s=0
    for q in a:s+=q;b+=s,
    l=0;h=10**9
    while l<h:
        v=l+h>>1;i=bisect(a,v)
        if s-b[i]-v*(n-i)<m:h=v
        else:l=v+1
    return l-1

print(bin_trees(N, M, sorted(Woods)))