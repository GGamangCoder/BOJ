N = int(input())

trees = [[] for _ in range(N)]   # 왼쪽([0]), 오른쪽([1]) 자식 노드
temp = list(map(int, input().split()))

# 부모 노드에 대해서,
for i in range(N):
    trees[i] = temp[i]

def delete(node):
    global trees
    trees[node] = -2
    for i in range(N):
        if trees[i] == node:
            delete(i)

remove_node = int(input())
delete(remove_node)

cnt = 0
for i in range(N):
    if trees[i] != -2:
        for node in trees:
            if node == i:
                break
        else:
            cnt += 1

print(cnt)
