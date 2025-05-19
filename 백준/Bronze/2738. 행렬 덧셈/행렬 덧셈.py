def get_matrix(row_length):
    matrix = []
    for _ in range(row_length):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    return matrix

def sum_matrix(A, B):
    result = []
    for i in range(N):
        temp = []
        for j in range(M):
            element = A[i][j] + B[i][j]
            temp.append(element)
        result.append(temp)
    return result

N, M = map(int, input().split())

matrix_A = get_matrix(N)
matrix_B = get_matrix(N)

result = sum_matrix(matrix_A, matrix_B)

for element in result:
    print(*element)