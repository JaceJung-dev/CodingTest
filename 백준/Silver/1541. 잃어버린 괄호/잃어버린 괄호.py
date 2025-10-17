import sys

input = sys.stdin.readline

equation = input().strip()
equation_split = equation.split("-")
n = len(equation_split)

total = sum(map(int, equation_split[0].split("+")))

for i in range(1, n):
    num = sum(map(int, equation_split[i].split("+")))
    total -= num

print(total)