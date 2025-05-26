current_hour, current_min = map(int, input().split())
cooking_time = int(input())

finish_time = current_hour * 60 + current_min + cooking_time

finish_hour = (finish_time // 60) % 24
finish_min = finish_time % 60

print(finish_hour, finish_min)

