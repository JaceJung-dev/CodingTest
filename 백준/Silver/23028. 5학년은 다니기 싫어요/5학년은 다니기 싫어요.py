import sys

input = sys.stdin.readline

N, major_credits, total_credits = map(int, input().split())
courses = [tuple(map(int, input().split())) for _ in range(10)]

semester_left = 8 - N

for i in range(semester_left):
    major, non_major = courses[i]

    major_credits_needed = max(0, 66 - major_credits)
    major_course_taken = min(major, 6, (major_credits_needed + 2) // 3)

    non_credits_needed = max(0, 130 - total_credits - major_course_taken * 3)
    non_course_taken = min(
        non_major, 6 - major_course_taken, (non_credits_needed + 2) // 3
    )

    major_credits += major_course_taken * 3
    total_credits += (major_course_taken + non_course_taken) * 3

if major_credits >= 66 and total_credits >= 130:
    print("Nice")
else:
    print("Nae ga wae")
