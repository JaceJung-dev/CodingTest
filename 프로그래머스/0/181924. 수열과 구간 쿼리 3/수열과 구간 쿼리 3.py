def solution(arr, queries):
    answer = []
    for array in queries:
        i = array[0]
        j = array[1]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    answer = arr
    return answer