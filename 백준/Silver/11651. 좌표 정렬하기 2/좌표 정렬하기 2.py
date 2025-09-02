import sys
input = sys.stdin.readline

def sort_rule(dots):
    x, y = dots.split()
    return int(y) + int(x) / 1000000

dots = sorted(sys.stdin.readlines()[1:], key=sort_rule)
print("".join(dots))