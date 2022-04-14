import sys
input = sys.stdin.readline
def solution():
    n = int(input().rstrip())
    string = []
    for i in range(n):
        string.append(input().rstrip())

    string = "".join(string)

    start = 0
    end = len(string) - 1
    ret = []
    count = 0

    while start <= end:
        index = select(string, start, end)
        char = string[index]
        count += 1
        ret.append(char)
        if count % 80 == 0:
            ret.append('\n')
        if index == start:
            start += 1
        else:
            end -= 1
    return "".join(ret)

def select(string, start, end):
    ret = start
    end_org = end
    if string[start] == string[end]:
        start += 1
        end -= 1
        while start < end and string[start] == string[end]:
            start += 1
            end -= 1

    if start < end:
        if string[start] > string[end]:
            ret = end_org

    return ret

print(solution())