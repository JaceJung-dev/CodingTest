import sys

input = sys.stdin.readline

def get_tree_length(trees, n):
    tree_len = 0
    for tree in trees:
        cut_len = tree - n
        if cut_len >= 0:
            tree_len += cut_len

    return tree_len

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
final_height = 0

while low <= high:
    middle = (low + high) // 2

    tree_len = get_tree_length(trees, middle)
    
    if tree_len >= M:
        final_height = middle
        low = middle + 1
    else:
        high = middle - 1

print(final_height)