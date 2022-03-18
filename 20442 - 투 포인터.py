import sys
def solution(string):
    start = 0
    end = len(string) - 1
    left_k_count = 0
    right_k_count = 0
    r_count = string.count('R')
    max_length = 0

    while start <= end:
        max_length = max(max_length, min(left_k_count, right_k_count) * 2 + r_count)
        if left_k_count <= right_k_count:
            start += 1
            while start < len(string):
                if string[start - 1] == 'K':
                    left_k_count += 1
                else:
                    r_count -= 1
                if string[start] == 'R':
                    break
                start += 1
        else:
            end -= 1
            while end >= 0:
                if string[end + 1] == 'K':
                    right_k_count += 1
                else:
                    r_count -= 1

                if string[end] == 'R':
                    break
                end -= 1

    return max_length
string = sys.stdin.readline().strip()
print(solution(string))