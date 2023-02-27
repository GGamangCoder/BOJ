# 트리 - Fail

N = int(input())

trees = [[0]*2 for _ in range(N+1)]
temp = list(map(int, input().split()))

# 트리 만들어주기
for i in range(N):     # 0번 노드 ~ N-1번 노드
    if temp[i] == -1:
        pass
    else:
        child, parent = i, temp[i]
        if not trees[parent+1][0]:
            trees[parent+1][0] = child + 1
        else:
            trees[parent+1][1] = child + 1


erase_node = int(input())
trees[erase_node] = [0, 0, 0]

def count_leaf(tree, node):
    global cnt
    if node != -1:
        if node == erase_node + 1:
            return
        if not tree[node+1][0] and not tree[node+1][1]:
            cnt += 1
            return
        count_leaf(tree, tree[node+1][0])
        count_leaf(tree, tree[node+1][1])

cnt = 0
count_leaf(trees, 0)
print(cnt)