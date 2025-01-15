def weapon_able(knight):
    count = 0
    for i in range(1, int(knight**0.5)+1):
        if knight % i == 0:
            count += 1
            if i != knight // i:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    for k in range(1, number+1):
        weapon = weapon_able(k)
        if weapon > limit:
            answer += power
        else:
            answer += weapon
    return answer
