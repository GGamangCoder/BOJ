lst = []
for i in range(1, 10):
    lst.append(int(input()))
lst.sort()
hap = sum(lst)
for i in range(8):
    for j in range(i+1, 9):
        if hap - lst[i] - lst[j] == 100:
            del lst[i]
            del lst[j-1]
            break
    if len(lst) != 9:
        break
for i in lst:
    print(i)