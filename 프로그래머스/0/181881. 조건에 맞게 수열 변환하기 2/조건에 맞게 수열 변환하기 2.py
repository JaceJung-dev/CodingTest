def solution(arr):
    answer = 0
    prev_arr = arr
    while True:
        curr_arr = []
        answer += 1
        for i in range(len(prev_arr)):
            if prev_arr[i] >= 50 and prev_arr[i] % 2 == 0:
                curr_arr.append(int(prev_arr[i] / 2))
            elif prev_arr[i] < 50 and prev_arr[i] % 2 == 1:
                curr_arr.append(prev_arr[i] * 2 + 1)
            else:
                curr_arr.append(prev_arr[i])
                
        if prev_arr == curr_arr:
            break
        else:
            prev_arr = curr_arr
            
    return answer-1