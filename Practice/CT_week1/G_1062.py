# 가르침

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = 0
words = [set(input().rstrip()[4:-4]) for _ in range(n)]
# 알파벳 배우는 내용에 따라 a ~ z 까지를 26개의 숫자 리스트에 담기
learn = [0] * 26
for s in 'acint':
    learn[ord(s) - ord('a')] = True

def dfs(idx, cnt):
    global ans

    if cnt == k - 5:
        temp = 0
        for word in words:
            flag = False
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    flag = True
                    break
            if not flag:
                temp += 1
        ans = max(ans, temp)
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

if k < 5:       # 최소 갯수
    print(0)
elif k == 26:   # 모든 알파벳
    print(n)
else:
    dfs(0, 0)
    print(ans)
