def solution(n, k, numbers):
    dp = [0] * len(numbers)
    start = 0
    while start < len(numbers):
        if numbers[start] % 2 == 0:
            break
        start += 1
    start_index = start
    count = 0
    max_count = 0
    remain_k_count = k
    for i in range(start, len(numbers)):
        if count == 0 and numbers[i] % 2 == 1:
            start_index = i + 1
            remain_k_count = k
            continue
        if numbers[i] % 2 == 0:
            count += 1
            max_count = max(count, max_count)
        else:
            if remain_k_count <= 0:
                while start_index < i and remain_k_count <= 0:
                    if numbers[start_index] % 2 == 0:
                        count -= 1
                    else:
                        remain_k_count += 1
                    start_index += 1
            remain_k_count -= 1

    return max_count

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(n, k, numbers))





