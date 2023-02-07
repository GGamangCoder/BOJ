from itertools import combinations

L, C = map(int, input().split())
alpha = sorted(list(map(str, input().split())))
vowels = ['a', 'e', 'i', 'o', 'u']

code_list = list(combinations(alpha, L))

for i in code_list:
    if ('a' in i) or ('e' in i) or ('i' in i) or ('o' in i) or ('u' in i):
        print(''.join(sorted(i)))