# 잃어버린 괄호

eq = input()
ans = 0
prev_val = ''
temp = ''
for s in eq:
    if s.isdigit():
        temp += s
    else:
        if s == '-':
            if prev_val == '-':
                ans -= int(temp)
            else:
                ans += int(temp)
                prev_val = '-'
        elif s == '+':
            if prev_val == '-':
                ans -= int(temp)
            else:
                ans += int(temp)
        temp = ''

if prev_val:
    ans -= int(temp)
else:
    ans += int(temp)
print(ans)