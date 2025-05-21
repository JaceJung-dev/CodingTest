pieces = [1, 1, 2, 2, 2, 8]

have_pieces = list(map(int, input().split()))
need_pieces = []
for i in range(len(pieces)):
    temp = pieces[i] - have_pieces[i]
    need_pieces.append(temp)

print(*need_pieces)