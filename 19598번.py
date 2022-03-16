import sys, heapq
def solution():
    input = sys.stdin.readline
    n = int(input())
    schedule = []
    max_time = 0
    for i in range(n):
        start, end = map(int, input().split())
        schedule.append((start, end))
        max_time = max(end, max_time)

    schedule.sort()
    endTime_heapq = []
    index = 0
    count = 0
    max_count = 0

    while index < len(schedule):
        time = schedule[index][0]
        while len(endTime_heapq) > 0 and endTime_heapq[0] <= time:
            heapq.heappop(endTime_heapq)
            count -= 1

        while index < len(schedule) and schedule[index][0] <= time:
            heapq.heappush(endTime_heapq, schedule[index][1])
            count += 1
            index += 1

        if count > max_count:
            max_count = count

    return max_count

print(solution())

