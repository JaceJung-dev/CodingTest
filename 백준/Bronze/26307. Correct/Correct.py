H, M = map(int, input().split())

start_time = 9 * 60
end_time = H * 60 + M
total_time = end_time - start_time

print(total_time)