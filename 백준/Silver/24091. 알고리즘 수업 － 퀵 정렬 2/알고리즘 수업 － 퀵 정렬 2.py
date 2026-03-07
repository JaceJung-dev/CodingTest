import sys
from sys import setrecursionlimit

setrecursionlimit(100000)

input = sys.stdin.readline


def partition(arr, p, r):
    global count, done

    x = arr[r]
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
            if count == K:
                done = True
                return i

    if i + 1 != r:
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        count += 1

        if count == K:
            done = True
            return i + 1

    return i + 1


def quick_sort(arr, p, r):
    global done
    if done:
        return
    if p < r:
        q = partition(arr, p, r)
        if done:
            return
        quick_sort(arr, p, q - 1)
        if done:
            return
        quick_sort(arr, q + 1, r)


if __name__ == "__main__":
    A, K = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    done = False

    quick_sort(arr, 0, A - 1)

    if not done:
        print(-1)
    else:
        print(*arr)
