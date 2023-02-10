s = input()
N = len(s)

small = 0           # 소괄호
big = 0             # 대괄호
for i in range(N):
    s = s.replace('()', '2')
    s = s.replace('[]', '3')
    