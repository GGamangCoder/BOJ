for _ in range(int(input())):
    s = input()
    for i in s:
        s = s.replace('()', '')
    print(s and 'NO' or 'YES')