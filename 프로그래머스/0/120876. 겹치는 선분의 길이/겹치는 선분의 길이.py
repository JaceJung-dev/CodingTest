def solution(lines):
    answer = 0  
    sets = [set(range(line[0], line[1])) for line in lines]

    answer = len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    return answer
