import sys
def get_input():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    return n, m, numbers
def solution(n, m, numbers):
    sum_array = [0] * (n + 1)
    remainder_array= [0] * m
    answer = 0

    for i in range(n):
        sum_array[i + 1] = (sum_array[i] + numbers[i]) % m

        if sum_array[i + 1] == 0:
            answer += 1
        remainder_array[sum_array[i + 1]] += 1

    for i in range(m):
        answer += (remainder_array[i] * (remainder_array[i] - 1)) // 2

    return answer
n, m, numbers = get_input()
print(solution(n, m, numbers))