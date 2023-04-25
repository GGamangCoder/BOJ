# 열쇠 (골드 1)
# 유형 - 

# 문을 나중에 딸 수도 있음 - 기억해놔야되나 ?


from collections import deque
import sys


input = sys.stdin.readline

# 방향 - 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global ans
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 영역 내에 있고 벽이 아니고, 미 방문일 때,
            if 0 <= nx < w + 2 and 0 <= ny < h + 2 and \
                graph[ny][nx] != '*' and not visited[ny][nx]:
                    next_point = graph[ny][nx]
                    # 대문자 문이면 두 가지 경우 - 키가 있거나/없거나
                    if 'A' <= next_point <= 'Z':
                        # 없으면 못 가고 다음 거 진행
                        if chr(ord(next_point) + 32) not in keys:
                            continue
                    # 만약 새로운 키를 발견하면 다시.. 초기화하고 탐색..
                    elif 'a' <= next_point <= 'z':
                        if next_point not in keys:
                            keys.add(next_point)
                            visited = [[False] * (w + 2) for _ in range(h + 2)]
                        # 아니면 상관없음, 진행은 그대로
                    elif graph[ny][nx] == '$':
                        ans += 1
                        graph[ny][nx] = '.'
                    
                    visited[ny][nx] = True
                    q.append((nx, ny))



T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().rstrip().split())
    # . 은 빈 공간, * 은 벽, $ 는 문서, A 는 문, a는 열쇠(대문자와 매칭)
    # 이 때 그래프는 시작점을 특정할 수 없어 패딩
    padding = list('.' * (w+2))
    graph = [padding] + [list('.' + input().rstrip() + '.') for _ in range(h)] + [padding]
    # 열쇠 정보
    keys = set(input().rstrip())
    ans = 0
    bfs()
    print(ans)
