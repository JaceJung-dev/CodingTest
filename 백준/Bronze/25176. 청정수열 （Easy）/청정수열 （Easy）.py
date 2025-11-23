import sys

input = sys.stdin.readline


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    n = int(input())
    answer = factorial(n)
    print(answer)


if __name__ == "__main__":
    main()
