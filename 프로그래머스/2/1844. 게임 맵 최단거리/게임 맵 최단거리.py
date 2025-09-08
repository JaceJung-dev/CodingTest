from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 시작이나 끝지점이 벽으로 되어있는 경우: 불가능(-1)
    if maps[0][0] == 0 or maps[h - 1][w - 1] == 0:
        return -1
    
    # 최단거리를 찾는 case >>> BFS
    # DFS를 사용하면 한 방향으로 끝까지 탐색하는 방식으로 모든 경로를 확인하고 최솟값을 선택하게 됨
    # BFS는 진행도중 도착지점에 도착하면 그것이 최단거리
    visited = [[False] * w for _ in range(h)]
    queue = deque([(0, 0, 1)])    # 행, 열, 움직인 횟수
    visited[0][0] = True
        
    while queue:
        row, col, count = queue.popleft()
        
        # 도착지점에 도착한 경우
        if row == h - 1 and col == w - 1:
            return count
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # 진영 밖으로 나가는 경우(제외)
            if not (0 <= new_row <= h - 1 and 0 <= new_col <= w - 1):
                continue
            
            # 이동한 곳이 처음 가는 곳이며, 벽이 아닌 경우(queue에 넣기)
            if not visited[new_row][new_col] and maps[new_row][new_col] == 1:
                queue.append((new_row, new_col, count + 1))
                visited[new_row][new_col] = True
    
    # 빈 칸을 모두 돌았지만, 도착지점에 도착 못한 경우
    return -1