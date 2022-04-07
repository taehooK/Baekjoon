from itertools import combinations
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution():
    n, m = map(int, input().split())

    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    homes_positions = []#1.1의 위치들
    store_positions = []#3.2의 위치들

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                homes_positions.append((i, j))
            elif board[i][j] == 2:
                store_positions.append((i, j))

    store_positions_combination = combinations(store_positions, m)  # 4.2의 위치들의 1부터 m 번째 까지의 조합
    for pos in store_positions:
        board[pos[0]][pos[1]] = 0

    min_distance = 1000000
    #3에서 구한조합 수만큼 반복
    for positions in store_positions_combination:
        cur_distance = 0
        for home_pos in homes_positions:
            distance = 1000000
            for pos in positions:
                distance = min(distance, abs(pos[0] - home_pos[0]) + abs(pos[1] - home_pos[1]))

            cur_distance += distance

        min_distance = min(min_distance, cur_distance)

    return min_distance
print(solution())
