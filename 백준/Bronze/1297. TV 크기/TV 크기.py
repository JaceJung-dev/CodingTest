D, H, W = map(int,input().split())

ratio = (D**2 / (H**2 + W**2))**0.5

real_height = int(H * ratio)
real_width = int(W * ratio)

print(real_height, real_width)