from collections import Counter
def solution(lines):
    answer = 0
    x_line = []
    for line in lines:
        for x in range(line[0], line[1]):
            x_line.append(x)
    
    count = Counter(x_line)
    for v in count.values():
        if v >= 2:
            answer += 1
            
    return answer
