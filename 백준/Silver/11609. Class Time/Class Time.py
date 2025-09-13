import sys
input = sys.stdin.readline

N = int(input())
students = [tuple(input().split()) for _ in range(N)]

students.sort(key=lambda x: (x[1], x[0]))

for student in students:
    print(student[0], student[1])