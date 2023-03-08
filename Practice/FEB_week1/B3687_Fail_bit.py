import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
code_list = []
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(1 << C):
    subset = []
    for j in range(C):
        if i & (1 << j):
            subset.append(alpha[j])
    if len(subset) == L:
        for j in vowels:
            if j in subset:
                code_list.append(sorted(subset))
                break
code_list.sort()
for i in code_list:
    print(''.join(i))

for i in range(1<<C):
    pass