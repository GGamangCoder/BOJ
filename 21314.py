# 민겸 수
# M 과 K 모두 자릿수

num = input()
N = len(num)
small = ['0'] * N
big = ['0'] * N

if num[0] == 'M':
    small[0] = big[0] = '1'
else:
    small[0] = big[0] = '5'

for i in range(1, N):
    if num[i] == 'M':
        if num[i-1] == 'M':
            small[i] = '0'
        else:
            small[i] = '1'
    else:
        small[i] = '5'

idx = 0           # M의 갯수, M 시작 인덱스
for i in range(1, N):
    if num[i] == 'K':
        if num[i-1] == 'K':
            big[i] = '5'
        else:
            big[i] = '0'
            big[idx] = '5'      # 처음 M은 5
        idx = i + 1
    else:
        if num[i-1] == 'M':
            big[i] = '0'
        elif num[i-1] == 'K':
            big[i] = '1'
            idx = i

print(''.join(big))
print(''.join(small))