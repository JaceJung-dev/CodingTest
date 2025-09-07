from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 시작이나 끝지점이 벽으로 되어있는 경우: 불가능(-1)
    if maps[0][0] == 0 or maps[h - 1][w - 1] == 0:
        return -1
    
    visited = [[False] * w for _ in range(h)]
    queue = deque([(0, 0, 1)])    # 행, 열, 움직인 횟수
    visited[0][0] = True
        
    while queue:
        row, col, count = queue.popleft()
        
        if row == h - 1 and col == w - 1:
            return count
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            if not (0 <= new_row <= h - 1 and 0 <= new_col <= w - 1):
                continue
            
            if not visited[new_row][new_col] and maps[new_row][new_col] == 1:
                queue.append((new_row, new_col, count + 1))
                visited[new_row][new_col] = True
                
    return -1