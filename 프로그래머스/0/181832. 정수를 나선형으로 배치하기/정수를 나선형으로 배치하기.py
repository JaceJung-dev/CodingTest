def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    
    num = 1
    while num <= n ** 2:
        # 오른쪽 진행
        for i in range(start_col, end_col + 1):
            answer[start_row][i] = num
            num += 1
            
        start_row += 1            
        # 아래로 진행
        for i in range(start_row, end_row + 1):
            answer[i][end_row] = num
            num += 1
        
        end_col -= 1
        
        # 왼쪽으로 진행
        for i in range(end_col, start_col -1, -1):
            answer[end_row][i] = num
            num += 1
        
        end_row -= 1
    
        # 위로 진행
        for i in range(end_row, start_row - 1, -1):
            answer[i][start_col] = num
            num += 1
        
        start_col += 1

    return answer