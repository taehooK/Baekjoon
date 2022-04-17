def solution():
    n = int(input())

    numbers = list(map(int, input().split()))

    left = 0
    right = n - 1
    ret = 0
    while left < right:
        value = (right - left - 1) * min(numbers[left], numbers[right])
        ret = max(value, ret)
        if numbers[left] < numbers[right]:
            left += 1
        else:
            right -= 1
    return ret


print(solution())