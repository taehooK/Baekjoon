from collections import deque
def solution():
    string = input()
    ret = []
    i = 0
    while i < len(string):
        if string[i] == '<':
            while i < len(string) and string[i] != '>':
                ret.append(string[i])
                i += 1
            ret.append(string[i])
            i += 1

        elif string[i] != ' ':
            queue = deque()
            while i < len(string) and string[i] != ' ' and string[i] != '<':
                queue.append(string[i])
                i += 1

            while queue:
                ret.append(queue.pop())
        else:
            ret.append(string[i])
            i += 1

    return "".join(ret)

print(solution())


