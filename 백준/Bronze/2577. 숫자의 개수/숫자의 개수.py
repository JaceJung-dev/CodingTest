A = int(input())
B = int(input())
C = int(input())

num_to_check = str(A * B * C)
num_count = [0] * 10

for num in num_to_check:
    num_count[int(num)] += 1
    
for count in num_count:
    print(count) 