def solution(name):
    # 위아래, 좌우는 서로 독립적이라 따로 계산하면 됨
    
    # 위아래 계산
    up_down_count = 0
    for char in name:
        up = ord(char) - ord("A")
        down = 26 - up
        up_down_count += min(up, down)
    
    # 좌우 계산
    l = len(name)
    left_right_count = l - 1             # 최악의 경우
    
    ## A가 있어서 건너뛸 구간 정의
    for i in range(l):
        j = i + 1
        while j < l and name[j] == "A":
            j += 1
        
        ## 건너뛴 구간을 찾고 경우의 수 계산
        case1 = i + i + (l - j)          # 일단 오른쪽으로 갔다가 유턴해서 마무리
        case2 = (l - j) + (l - j) + i    # 먼저 왼쪽으로 갔다가 유턴해서 마무리
            
        left_right_count = min(left_right_count, case1, case2)
    
    answer = up_down_count + left_right_count
    return answer