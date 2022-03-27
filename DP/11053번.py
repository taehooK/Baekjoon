def solution():
    n = int(input())
    array = list(map(int, input().split()))
    dp = [1] * n

    for i in range(1, n):
        max_count = 0
        for j in range(i - 1, -1, -1):
            if array[i] > array[j]:
                max_count = max(max_count, dp[j])

        dp[i] = max_count + 1

    print(max(dp))

solution()


