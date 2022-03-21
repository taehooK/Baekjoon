def solution(n, k, numbers):
    dp = [0] * len(numbers)
    start = 0
    while start < len(numbers):
        if numbers[start] % 2 == 0:
            break
        start += 1
    dp_index = 0
    is_even = True
    count = 0
    dp_count = 0
    for i in range(start, len(numbers)):
        if is_even and numbers[i] % 2 == 1:
            is_even = False
            dp[dp_index] = count
            dp_index += 1
            dp_count += 1
            count = 0
        elif not is_even and numbers[i] % 2 == 0:
            is_even = True
            dp[dp_index] = count
            dp_index += 1
            dp_count += 1
            count = 0
        count += 1

    dp[dp_index] = count
    dp_count += 1

    max_count = 0
    remain_k = k
    start_index = 0
    count = 0
    for i in range(dp_count):
        if i % 2 == 0:
            count += dp[i]
            max_count = max(max_count, count)
        else:
            if dp[i] > remain_k:
                count -= dp[start_index]
                remain_k += dp[start_index + 1]
                start_index += 2
                while start_index < i and dp[i] > remain_k and remain_k < k:
                    count -= dp[start_index]
                    remain_k += dp[start_index + 1]
                    start_index += 2
                remain_k -= dp[i]
            else:
                remain_k -= dp[i]

    return max_count

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(n, k, numbers))


