def solution(n):
    a, b = 1, 2
    if n == 1:
        return a
    elif n == 2:
        return b

    for i in range(3, n + 1):
        a, b = b, a + b

    return b % 1234567