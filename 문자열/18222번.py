def solution(k):
    two_power = 1
    while two_power < k:
        two_power *= 2
    count = 0
    while k > 1:
        count += 1
        while two_power >= k:
            two_power //= 2
        k -= two_power

    ret = 1

    if count % 2 == 0:
        ret = 0
    return ret

k = int(input())
print(solution(k))
