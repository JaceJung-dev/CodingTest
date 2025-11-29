import sys

input = sys.stdin.readline


def get_number_of_divisors(n):
    count = 0
    rs = int(n**0.5)
    for i in range(1, rs + 1):
        if n % i == 0:
            count += 2
    if rs * rs == n:
        count -= 1

    return count


T = int(input())

for _ in range(T):
    N = int(input())

    count = get_number_of_divisors(N)
    print(N, count)
