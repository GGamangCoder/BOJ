from itertools import combinations

L, C = map(int, input().split())
alpha = sorted(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
code_list = list(combinations(alpha, L))

for code in code_list:
    vowel = cons = 0    # 모음, 자음
    for word in code:
        if word in vowels:
            vowel += 1
        else:
            cons += 1
    if vowel >= 1 and cons >= 2:
        print(''.join(code))