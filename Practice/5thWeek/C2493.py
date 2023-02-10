N = int(input())        # 1 <= N <= 500,000
high_list = list(map(int, input().split())) # 1 <= h <= 100,000,000

# for i in range(N-1, -1, -1):
#     flag = False
#     for j in range(i, -1, -1):
#         if high_list[i] < high_list[j]:
#             high_list[i] = j + 1
#             flag = True
#             break
#     if flag == False:
#         high_list[i] = 0
# print(*high_list)


ans = []
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > high_list[i]:
            ans.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, high_list[i]])     # [index, big high]

print(*ans)