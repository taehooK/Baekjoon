def get_input():
    n = int(input())
    return n

def solution(n):
    dp = [5000] * (n + 1)
    if n >= 3:
        dp[0] = 0
        dp[3] = 1
        for i in range(5, n + 1):
            dp[i] = min(dp[i - 3] + 1, dp[i])
            dp[i] = min(dp[i - 5] + 1, dp[i])
    if dp[n] >= 5000:
        return -1
    return dp[n]

n = get_input()
print(solution(n))
