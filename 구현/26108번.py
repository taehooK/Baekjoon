import sys
import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def get_input():
    input = sys.stdin.readline
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n * n)]

    return n, info

def solution(n, info_array):
    area = [[0 for i in range(n)] for i in range(n)]
    like_friends = dict()
    for info in info_array:
        dict_temp = {}
        for i in range(1, 5):
            dict_temp[info[i]] = True
        like_friends[info[0]] = dict_temp
    #info 개수만큼 반복
    for info in info_array:
        number = info[0]
        friends = like_friends[number]
        row, column = step(area, friends)
        area[row][column] = number
    return get_satisfaction(area, like_friends)

def get_satisfaction(area, like_friends):
    sum = 0
    for i in range(len(area)):
        for j in range(len(area)):
            count = 0
            number = area[i][j]
            friends = like_friends[number]
            for k in range(4):
                row = i + dy[k]
                column = j + dx[k]
                if 0 <= row < len(area) and 0 <= column < len(area):
                    if area[row][column] in friends:
                        count += 1
            if count > 0:
                value = pow(10, count - 1)
                sum += value
    return sum

def step(area, friends):
    candidates = []

    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] > 0:
                continue
            count = 0
            for k in range(4):
                row = i + dy[k]
                column = j + dx[k]
                if 0 <= row < len(area) and 0 <= column < len(area):
                    if area[row][column] in friends:
                        count += 1
            heapq.heappush(candidates, (-count, i, j)) #인접 수, 행, 열
    candidate = heapq.heappop(candidates)
    next_candidates = list()
    next_candidates.append((candidate[1], candidate[2]))
    limit = candidate[0]
    while candidates:
        candidate = heapq.heappop(candidates)
        if candidate[0] > limit:
            break
        next_candidates.append((candidate[1], candidate[2]))

    # 후보들 재설정 하기
    candidate = next_candidates[0]
    row = candidate[0]
    column = candidate[1]
    if len(next_candidates) > 1: # 최상위권 인접 수 두명의 개수가 같으면 재탐색
        candidates.clear()
        for candidate in next_candidates:
            row = candidate[0]
            column = candidate[1]
            if area[row][column] > 0:
                continue
            count = 0
            for k in range(4):
                next_row = row + dy[k]
                next_column = column + dx[k]
                if 0 <= next_row < len(area) and 0 <= next_column < len(area):
                    if area[next_row][next_column] == 0:
                        count += 1
            heapq.heappush(candidates, (-count, row, column))  # 인접 수, 행, 열
        candidate = heapq.heappop(candidates)
        row = candidate[1]
        column = candidate[2]

    return row, column

n, info = get_input()
print(solution(n, info))





