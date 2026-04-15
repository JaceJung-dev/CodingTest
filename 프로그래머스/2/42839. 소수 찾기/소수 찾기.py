from itertools import permutations


def solution(numbers):
    def fact(n):
        if n == 0:
            return 1

        return n * fact(n - 1)

    answer = 0
    N = 9999999
    is_prime = [True] * (N + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(N**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False
            
    seen = set()

    for n in range(1, len(numbers) + 1):
        for perm in permutations(numbers, n):
            num = int("".join(perm))
            if num not in seen:
                answer += is_prime[num]
            seen.add(num)

    return answer
