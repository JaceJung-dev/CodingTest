all_students = set(range(1,31))
do_homework = set()
for _ in range(28):
    n = int(input())
    do_homework.add(n)
    
no_homework = list(all_students - do_homework)
no_homework.sort()

for i in no_homework:
    print(i)

