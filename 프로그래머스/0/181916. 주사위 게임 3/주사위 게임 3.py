def count_dice(arr):
    count = [0] * 6
    for num in arr:
        count[num - 1] += 1
    return count


def solution(a, b, c, d):
    answer = 0
    dice_res = [a, b, c, d]
    dice_count = count_dice(dice_res)

    if 4 in dice_count:
        p = dice_count.index(4) + 1
        answer = 1111 * p
    elif 3 in dice_count:
        p = dice_count.index(3) + 1
        q = dice_count.index(1) + 1
        answer = (10 * p + q) ** 2
    elif 2 in dice_count and 1 not in dice_count:
        temp = []
        for i in range(len(dice_count)):
            if dice_count[i] == 2:
                temp.append(i + 1)
        p, q = temp[0], temp[1]
        answer = (p + q) * abs(p - q)
    elif 2 in dice_count and 1 in dice_count:
        temp = []
        for i in range(len(dice_count)):
            if dice_count[i] == 1:
                temp.append(i + 1)
        q, r = temp[0], temp[1]
        answer = q * r
    else:
        answer = dice_count.index(1) + 1
    return answer