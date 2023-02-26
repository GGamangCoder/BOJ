# 트리 순회 - 이진 트리, 전위/중위/후위 순회

def pre_order(tree, node):
    if node != False:
        print(alpha[node], end='')
        pre_order(tree, tree[node][0])
        pre_order(tree, tree[node][1])


def in_order(tree, node):
    if node != False:
        in_order(tree, tree[node][0])
        print(alpha[node], end='')
        in_order(tree, tree[node][1])

def post_order(tree, node):
    if node != False:
        post_order(tree, tree[node][0])
        post_order(tree, tree[node][1])
        print(alpha[node], end='')


N = int(input())        # 노드 갯수
# value, left, right
trees = [0] * (N+1)     # 트리 상태 만들기
alpha = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(N):
    temp = input().split()
    trees[alpha.index(temp[0])] = [alpha.index(temp[1]), alpha.index(temp[2])]

pre_order(trees, 1)
print()
in_order(trees, 1)
print()
post_order(trees, 1)