def solution(my_string, queries):
    answer = ''
    for query in queries:
        s, e = query[0], query[1]
        if s != 0:
            my_string = my_string[0:s] + my_string[e:s-1:-1] + my_string[e+1:]
        else:
            my_string = my_string[e::-1] + my_string[e+1:]
    answer = my_string
    return answer