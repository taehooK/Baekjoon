import heapq
import sys

#난이도별 우선순위 큐 배열
#우선순위 큐 (난이도, 문제번호)
class Data:
    def __init__(self, number, level):
        self.number = number
        self.level = level

    def __lt__(self, other):
        if self.level != other.level:
            return self.level > other.level
        return self.number > other.number

def solution():
    input = sys.stdin.readline
    n = int(input())
    desc_level_q = []
    asc_level_q = []
    levels = dict()

    for i in range(n):
        number, level = map(int, input().split())
        heapq.heappush(desc_level_q, Data(number, level))
        heapq.heappush(asc_level_q,Data(-number, -level))
        levels[number] = level
    solved = dict()

    m = int(input())
    for i in range(m):
        object = input().split()

        if object[0] == 'recommend':
            number = int(object[1])
            if number == 1:
                while desc_level_q:
                    data = desc_level_q[0]
                    if (data.number, data.level) in solved:
                        heapq.heappop(desc_level_q)
                    else:
                        print(data.number)
                        break
            elif number == -1:
                while asc_level_q:
                    data = asc_level_q[0]
                    if (-data.number, -data.level) in solved:
                        heapq.heappop(asc_level_q)
                    else:
                        print(-data.number)
                        break

        elif object[0] == 'solved':
            number = int(object[1])
            solved[(number, levels[number])] = True

        elif object[0] == 'add':
            number = int(object[1])
            level = int(object[2])
            levels[number] = level
            heapq.heappush(desc_level_q, Data(number, level))
            heapq.heappush(asc_level_q, Data(-number, -level))

solution()

