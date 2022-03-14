#점화식
#dp[i] = dp[i - 1] + dp[i + 1]

def solution(n):
    dp = [0] * (n + 1)

    if n == 1:
        return 1

    dp[1] = 1
    dp[2] = 2

    i = 3
    while i <= n:
        dp[i] = (dp[i -  1] + dp[i - 2]) % 10007

        i += 1
    return dp[n]

n = int(input())
print(solution(n))

