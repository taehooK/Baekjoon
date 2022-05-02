import sys

input = sys.stdin.readline

def solution(string):
    start = 0
    end = len(string) - 1
    ret = 2 # default = 유사회문 X

    while start <= end and string[start] == string[end]:
        start += 1
        end -= 1

    if start > end:
        ret = 0
    elif is_palindrome(string, start + 1, end) or is_palindrome(string, start, end - 1):
        ret = 1

    return ret;


def is_palindrome(string, start, end):
    start_t = start
    end_t = end
    while start_t <= end_t and string[start_t] == string[end_t]:
        start_t += 1
        end_t -= 1
    if start_t > end_t:
        return True
    return False


t = int(input())
for _ in range(t):
    print(solution(input().rstrip()))



