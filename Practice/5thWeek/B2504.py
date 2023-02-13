s = input()
length = len(s)

stack = []
temp = 1
res = 0
for i in range(length):
    # 열린 괄호, 누적하여 계산됨
    brk = s[i]  # bracket 줄임
    if brk == '(':
        temp *= 2
        stack.append(brk)
    elif brk == '[':
        temp *= 3
        stack.append(brk)

    # 괄호 닫을 때, 계산 진행
    elif brk == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if s[i-1] == '(':
            res += temp
        temp //= 2
        stack.pop()
    elif brk == ']':
        if not stack or stack[-1] == '(':
            res = 0
            break
        if s[i-1] == '[':
            res += temp
        temp //= 3
        stack.pop()

if stack:
    res = 0
print(res)