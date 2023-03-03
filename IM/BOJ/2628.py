#  종이자르기

r, c = map(int, input().split())
n = int(input())
# 종이가 잘리우는 r, c 위치
cut_row = [0, r]
cut_col = [0, c]
for i in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        cut_col.append(temp[1])
    else:
        cut_row.append(temp[1])

cut_col.sort()
cut_row.sort()
dp_c = []
dp_r = []
for i in range(len(cut_col)-1):
    dp_c.append(cut_col[i+1] - cut_col[i])
for i in range(len(cut_row)-1):
    dp_r.append(cut_row[i+1] - cut_row[i])
print(max(dp_c) * max(dp_r))