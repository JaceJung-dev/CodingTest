def solution(rank, attendance):
    answer = 0
    students = []
    for i in range(1, len(rank) + 1):
        idx = rank.index(i)
        if attendance[idx] == True:
            students.append(idx)
    answer = students[0] * 10000 + students[1] * 100 + students[2]
    return answer