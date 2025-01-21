def solution(array, height):
    taller_list = [person for person in array if person > height]
    answer = len(taller_list)
    return answer