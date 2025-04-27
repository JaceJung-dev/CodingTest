def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query[0], query[1], query[2]
        temp = []
        for i in range(s, e+1):
            if arr[i] > k:
                temp.append(arr[i])
        if len(temp) == 0:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer