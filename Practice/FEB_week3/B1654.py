# 랜선 자르기
# 이분 탐색(Binary Search)

K, N = map(int, input().split())
# K <= 10,000 & N <= 1,000,000

line = [int(input()) for _ in range(K)]

def find_max(arr, ans):          # 랜선 상태, 목표
    s, e = 1, max(arr)
    while s <= e:
        mid = (s + e) // 2
        res = 0
        for ln in arr:
            res += ln // mid
        
        if res >= ans:
            s = mid + 1
        else:
            e = mid - 1

    return e

ans = find_max(line, N)

print(ans)