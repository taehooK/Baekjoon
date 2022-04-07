def solution(n, m, numbers):
    min_num = min(numbers)

    start_time = 0
    end_time = min_num * m
    minMiddle = 0

    while start_time <= end_time:
        middle = (start_time + end_time) // 2
        count = 0
        for number in numbers:
            count += middle // number
        if count < m:
            start_time = middle + 1
        else:
            end_time = middle - 1
            minMiddle = middle

    return minMiddle

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

print(solution(n, m, numbers))

