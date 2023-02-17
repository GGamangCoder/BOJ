N = int(input())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
print('\n'.join(sorted(map(str, lst))))