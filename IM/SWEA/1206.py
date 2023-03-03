# IM - View(1206)

import sys
sys.stdin = open("input.txt")


def check_build(arr):
    ans = 0
    max
    for i in range(2, N-2):
        cur_b = arr[i]
        l, r = max(arr[i-2], arr[i-1]), max(arr[i+1], arr[i+2])
        if cur_b > l and cur_b > r:
            temp = cur_b - max(l, r)
            ans += temp

    return ans


for tc in range(1, 11):
    N = int(input())        # 건물 갯수
    builds = list(map(int, input().split()))    # 총 N개, 실제 N-4개

    print(f'#{tc} {check_build(builds)}')