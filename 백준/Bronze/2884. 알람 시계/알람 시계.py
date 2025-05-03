H, M = map(int, input().split())

total_time = H * 60 + M
changed_time = 0
if total_time < 45:
    changed_time = 1440 + total_time - 45
else:
    changed_time = total_time - 45
    
print(changed_time // 60, changed_time % 60)