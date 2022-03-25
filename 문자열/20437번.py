import sys
def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        string = input().strip()
        k = int(input())

        max_length = -1
        min_length = 10e6
        words_positions = dict()

        for i in range(97, 123):
            words_positions[chr(i)] = []

        for i in range(len(string)): # \n문자 앞까지
            words_positions[string[i]].append(i)

        for word_pos in words_positions.values():
            if len(word_pos) < k:
                continue
            start = 0
            end = start + (k - 1)
            while end < len(word_pos):
                first = 0
                if start - 1 >= 0:
                    first = word_pos[start - 1] + 1
                last = len(string) - 1
                if end + 1 < len(word_pos):
                    last = word_pos[end + 1] - 1

                distance = word_pos[end] - word_pos[start] + 1
                min_length = min(min_length, distance)
                max_length = max(max_length, distance)
                start += 1
                end += 1
        if min_length == 10e6 or max_length == -1:
            print(-1)
        else:
            print(min_length, max_length)

solution()