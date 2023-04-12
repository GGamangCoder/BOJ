# 공유기 설치
# 양쪽 끝에서부터 안쪽으로 설치해주자.
# 결과 최솟값은 1, 거리를 출력해주는 문제 .
# 출처 - https://hyojeong94.tistory.com/151 

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
# 정렬
lst.sort()
# 시작, 최소 거리
start = 1   
# 끝, 최대 거리
end = lst[-1] - lst[0]
# 결과 거리 값
ans = 0
while start <= end:
    # 거리의 중간값
    mid = (start + end) // 2
    val = lst[0]
    # 공유기 갯수
    cnt = 1
    for i in range(1, len(lst)):
        if lst[i] >= val + mid:
            val = lst[i]
            cnt += 1
    
    if cnt >= C:
        # 갯수가 많으면 시작을 늘려
        start = mid + 1
        ans = mid
    else:
        # 적으면 최대치를 줄여줘
        end = mid -1

print()