def solution(array, commands):
    answer = []
    for command in commands:
        s, e, k = command[0], command[1], command[2]
        arr = array[s - 1: e]
        arr.sort()
        answer.append(arr[k - 1])
    return answer