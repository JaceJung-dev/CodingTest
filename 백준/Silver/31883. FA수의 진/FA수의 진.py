import sys

input = sys.stdin.readline

N = int(input())
total_time = 0
for i in range(N):
    crosswalk, bridge, green, red = map(int, input().split())
    cycle = green + red
    cycle_time = total_time % cycle

    if cycle_time < green:
        wait_time = 0
    else:
        wait_time = green + red - cycle_time

    cross_time = total_time + wait_time + crosswalk
    bridge_time = total_time + bridge

    total_time = min(cross_time, bridge_time)

print(total_time)
