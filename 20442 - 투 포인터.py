def solution(string):
    position = [0, len(string) - 1]
    counts = [0] * 2
    r_count = string.count('R')
    max_length = 0

    while position[0] <= position[1]:
        length = min(counts[0], counts[1]) * 2 + r_count
        max_length = max(max_length, length)

        index = 0
        i = position[0] + 1
        offset = 1
        if counts[0] > counts[1]:
            index = 1
            i = position[1] - 1
            offset = -1

        while 0 <= i < len(string):
            if string[i - offset] == 'K':
                counts[index] += 1
            else:
                r_count -= 1
            if string[i] == 'R':
                break
            i += offset

        position[index] = i
    return max_length

string = input()
print(solution(string))



