import sys
input = sys.stdin.readline
 
def calculate_pos(pos, time, limit):
    total = pos + time
    cycle = 2 * limit
    position = total % cycle
    
    return position if position <= limit else 2 * limit - position

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = calculate_pos(p, t, w)
y = calculate_pos(q, t, h)

print(x, y)