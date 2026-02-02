import sys

input = sys.stdin.readline

GRADE_MAP = {
    "A+": 450,
    "A0": 400,
    "B+": 350,
    "B0": 300,
    "C+": 250,
    "C0": 200,
    "D+": 150,
    "D0": 100,
    "F": 0,
}

N, X = input().split()
N = int(N)

a, b = X.split(".")
X = int(a) * 1000 + int(b) * 10  # 기준 평균 ×1000

credit_sum = 0
score_sum = 0
for _ in range(N - 1):
    credit, grade = input().split()
    credit = int(credit)

    credit_sum += credit
    score_sum += credit * GRADE_MAP[grade]

last_credit = int(input())
credit_sum += last_credit

grades = ["F", "D0", "D+", "C0", "C+", "B0", "B+", "A0", "A+"]

min_grade = None
for grade in grades:
    new_score = score_sum + last_credit * GRADE_MAP[grade]
    avg = (new_score // credit_sum) * 10

    if avg > X:
        min_grade = grade
        break

if min_grade:
    print(min_grade)
else:
    print("impossible")
