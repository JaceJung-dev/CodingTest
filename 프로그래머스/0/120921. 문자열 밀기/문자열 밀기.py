def solution(A, B):
    count = 0
    for i in range(len(A)):
        if A == B:
            return count 
        count += 1
        A = A[-1] + A[0:-1]
    return -1