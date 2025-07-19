import sys
input = sys.stdin.readline

n, d = map(int, input().split())

start_num = 10 ** (n-1)
end_num = 10 ** n

is_answer = False
answer_num = 0

for num in range(start_num, end_num):
    if num % d == 0:
        answer_num = num
        break
        
if answer_num:
    print(answer_num)
else:
    print("No solution")