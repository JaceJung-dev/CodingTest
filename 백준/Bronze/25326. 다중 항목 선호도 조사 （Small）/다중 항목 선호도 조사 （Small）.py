import sys

input = sys.stdin.readline

choices = {}
subjects = ["kor", "eng", "math"]
fruits = ["apple", "pear", "orange"]
colors = ["red", "blue", "green"]

N, M = map(int, input().split())
for _ in range(N):
    choice = tuple(input().split())

    choices[choice] = choices.get(choice, 0) + 1

for _ in range(M):
    subject, fruit, color = input().split()

    s_cases = subjects if subject == "-" else [subject]
    f_cases = fruits if fruit == "-" else [fruit]
    c_cases = colors if color == "-" else [color]

    count = 0
    for s in s_cases:
        for f in f_cases:
            for c in c_cases:
                choice = (s, f, c)
                count += choices.get(choice, 0)

    print(count)
