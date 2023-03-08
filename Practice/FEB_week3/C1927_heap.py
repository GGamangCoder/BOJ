# 최소 힙
# 1. 배열에 자연수 x를 넣는다  - insert
# 2. 배열에서 가장 작은 값을 출력하고 제거한다 - pop
# 0이면 pop, 없으면 0

# Heap up, 힙 업, 아래에서부터 위로 
def insert(tree, node):
    c = len(tree)   # 마지막 인덱스, 최근에 들어온 값
    tree.extend([node])     #  그리고 확장
    p = c // 2
    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def heap_pop(tree):
    size = len(tree) - 1        # 실제 크기
    # val = tree[1]               # 가장 첫 번째 요소 임시저장
    size -= 1                   # 하나 빼줄거니까
    tree[1], tree[-1] = tree[-1], tree[1]          # 가장 마지막 값을 앞으로 땡겨와, 최상단 노드
    p = 1           # 맨 위를 부모 노드로
    left = 2*p        # 왼쪽을 자식 노드로
    while left <= size:          # 마지막꺼는 또 비교해주면 안돼
        if left + 1 <= size and tree[left] > tree[left + 1]:    # 오른쪽이 더 작으면
            left += 1           # 비교대상 오른쪽으로 바꿔주기
        if tree[left] < tree[p]:        # 부모 노드가 더 크면 작은 걸 위로 올려주고 반복
            tree[left], tree[p] = tree[p], tree[left]
            p = left
            left, right = 2*p, 2*p+1
        else:
            break

    return tree.pop()       # 마지막 요소에 저장된 최솟값을 추출


def min_heap(tree, node):
    if node == 0:       # pop하는 경우,
        if len(tree) > 1:   # 최초 넣어준 게 있어서 .. 빈 값
            res = heap_pop(tree)        # 팝한 결과, 그리고 정렬까지
            print(res)
        else:
            print(0)
    else:               # 숫자가 들어오는 경우
        insert(tree, node)


N = int(input())
tree = [0]
for i in range(N):
    node = int(input())
    min_heap(tree, node)

