# 리그 오브 레게노 (골드 2)
# 위상정렬

# 출처 - https://chinpa.tistory.com/133 


import sys
input = sys.stdin.readline

n = int(input())
items = dict()
for _ in range(n):
    i1, i2 = input().split()
    try:
        items[i1]["list"].append(i2)
    except:
        items[i1] = dict()
        items[i1]["list"] = [i2]
        items[i1]["count"] = 0

    try:
        items[i2]["count"] += 1
    except:
        items[i2] = dict()
        items[i2]["list"] = []
        items[i2]["count"] = 1

buy_list, answer = [], []

for key in items.keys():
    if items[key]["count"] == 0:
        buy_list.append(key)

while buy_list:
    next_list = []
    for key in sorted(buy_list):
        for conn_item in items[key]["list"]:
            items[conn_item]["count"] -= 1
            if items[conn_item]["count"] == 0:
                next_list.append(conn_item)
        answer.append(key)

    buy_list = next_list

if len(answer) == len(items):
    for ans in answer:
        print(ans)
else:
    print(-1)