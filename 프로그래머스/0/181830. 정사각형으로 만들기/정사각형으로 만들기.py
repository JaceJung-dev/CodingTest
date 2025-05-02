def solution(arr):
    answer = []
    row_len = len(arr)
    column_len = len(arr[0])
    
    if row_len > column_len:
        for column in arr:
            for _ in range(row_len - column_len):
                column.append(0)
            answer.append(column)    
    elif row_len < column_len:
        for _ in range(column_len - row_len):
            temp = [0] * column_len
            arr.append(temp)
            answer = arr
    else:
        answer = arr
            

    return answer