import math

N = int(input())
layer = math.ceil((3 + math.sqrt(12 * N - 3)) / 6)

print(layer)
