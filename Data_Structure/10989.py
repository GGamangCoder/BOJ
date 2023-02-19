import sys
N = int(sys.stdin.readline())
lst = [0]*10000
for i in range(N):
    lst[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if lst[i] != 0:
        for _ in range(lst[i]):
            print(i+1)