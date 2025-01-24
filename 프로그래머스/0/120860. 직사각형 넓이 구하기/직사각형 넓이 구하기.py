def solution(dots):
    answer = 0
    x_dots = list({dot[0] for dot in dots})
    y_dots = list({dot[1] for dot in dots})
    x_len = abs(x_dots[0] - x_dots[1])
    y_len = abs(y_dots[0] - y_dots[1])

    answer = x_len * y_len

    return answer