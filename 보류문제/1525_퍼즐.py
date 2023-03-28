# 퍼즐 문제(#1525) - 골드2

import sys
from collections import deque


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
def bfs():
    q = deque([graph])
    visited[graph] = 0
    
    while q:
        # 현재 상태를 나타내는 변수
        status = q.popleft()
        
        if status == '123456780':
            return visited[status]

        zero_idx = status.find('0')
        x, y = zero_idx // 3, zero_idx % 3
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_idx = nx * 3 + ny
                # 문자열은 immmutable 하므로
                status_list = list(status)
                status_list[zero_idx], status_list[new_idx] = status_list[new_idx], status_list[zero_idx]
                # 현재 상태 초기화
                new_status = ''.join(status_list)
                
                if not visited.get(new_status):
                    visited[new_status] = visited[status] + 1   # 누적
                    q.append(new_status)

    # 탐색 끝난 후 올바른 리턴값이 발생하지 않으면,
    return -1


# 하나의 문자열로 왼쪽 상단부터 오른쪽 하단에 대해 저장
graph = ""
for _ in range(3):
    graph += ''.join(input().split())

visited = dict()

print(bfs())