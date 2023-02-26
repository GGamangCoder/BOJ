# 트리

N = int(input())

trees = [[0]*3 for _ in range(N+1)]
temp = list(map(int, input().split()))

# 트리 만들어주기
for i in range(N):     # 0번 노드 ~ N-1번 노드
    if temp[i] == -1:
        pass
    else:
        child, parent = i+1, temp[i] + 1
        if not trees[parent][0]:
            trees[parent][0] = child
        else:
            trees[parent][1] = child

        trees[child][2] = parent

erase_node = int(input())
trees[erase_node+1] = [0, 0, 0]

def count_leaf(tree, node):
    global cnt
    if node > N:
        return
    if not tree[node][0] and not tree[node][1]:
        if node == erase_node+1:
            return
        cnt += 1
        return
    count_leaf(tree, tree[node][0])
    count_leaf(tree, tree[node][1])

cnt = 0
count_leaf(trees, 1)
print(cnt)