def solution(n):
    dp = [[1 for i in range(10)] for i in range(n + 1)]
    dp[1][0] = 0

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000

    return sum(dp[n]) % 1000000000

n = int(input())
print(solution(n))

