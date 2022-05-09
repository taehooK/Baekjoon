def solution():
    n, k = map(int, input().split())
    numbers = [i for i in range(n + 1)]
    count = 0
    for i in range(2, n + 1):
        if numbers[i] == i:
            j = 1
            value = i * j
            while value <= n:
                if numbers[value] == value:
                    numbers[value] = -1
                    count += 1
                if count == k:
                    return value
                j += 1
                value = i * j

    return -1

print(solution())
print(solution())
print(solution())
print(solution())
print(solution())




