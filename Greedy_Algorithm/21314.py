s = input()
stack_small = []
stack_big = []
small = ''
big = ''
for si in s:
    if si == 'M':
        stack_small.append(si)
        stack_big.append(si)
    elif si == 'K':
        if stack_small:
            small += '1' + '0' * (len(stack_small)-1)
            stack_small = []
        small += '5'
        
        if not stack_big:
            big += '5'
        else:
            big += '5' + '0' * len(stack_big)
            stack_big = []
# 끝에 M이 스택에 남아있을 경우
if stack_small:
    small += '1' + '0' * (len(stack_small)-1)

if stack_big:
    big += '1' * len(stack_big)

print(big, small, sep='\n')