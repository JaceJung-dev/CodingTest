def cal_num(a, b):
    return (a + b) * (a - b)

A, B = map(int, input().split())

print(cal_num(A, B))