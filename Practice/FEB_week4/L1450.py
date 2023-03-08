# 냅색 문제
## "Meet in the middle" 알고리즘

# N개의 물건, 최대 C만큼의 무게 넣을 수 있는 가방
n, c = map(int, input().split())
stuff = list(map(int, input().split()))
# 두 개의 부류로 나누어주기
# 각각에 대해 탐색해준 뒤,
# 첫 번째 그룹 요소 하나하나에 대해 오른쪽 그룹과 매칭하여 비교
stuff1, stuff2 = stuff[:n//2], stuff[n//2:]
left, right = [], []

def brute_force(lst, idx, ):
    if len(lst) == idx
    pass


def binary_search():
    pass