total_time = 0

for _ in range(4):
    input_time = int(input())
    total_time += input_time
    
print(total_time // 60)
print(total_time % 60)