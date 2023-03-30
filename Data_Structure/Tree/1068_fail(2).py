# 트리 - Fail

N = int(input())

trees = [[] for _ in range(N)]   # 왼쪽([0]), 오른쪽([1]) 자식 노드
temp = list(map(int, input().split()))

# 트리 만들어주기
for i in range(N):
    if temp[i] == -1:
        pass
    else:
        # 자식 노드들 추가해주기
        trees[temp[i]].append(i)

remove_node = int(input())
trees[remove_node] = [-1]

cnt = 0
def counting_leaf(tree, node):
    global cnt
    if node != N:
        if not tree[node]:
            if node == remove_node:
                return
            cnt += 1
            return
        else:
            for i in range(len(tree[node])):
                counting_leaf(tree, tree[node][i])

counting_leaf(trees, 0)
print(cnt)
