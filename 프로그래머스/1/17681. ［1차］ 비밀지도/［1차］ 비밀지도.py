def solution(n, arr1, arr2):
    bi_list = []
    answer = []
    for i in range(n):
        bi_list.append((bin(arr1[i] | arr2[i])[2:]).zfill(n))

    for num in bi_list:
        answer.append(num.replace('1',"#").replace('0', " "))
    return answer