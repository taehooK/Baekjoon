import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    board = [list(map(int, input().strip())) for i in range(n)]
    if n == 1 and m == 1:
        return 1

    board_3d = [[item[:] for item in board], [item[:] for item in board]]

    queue = deque() # row, column, 벽을 부술 기회가 남아있는지 여부
    queue.append(((0, 0, 1, True)))
    board_3d[0][0][0] = -1
    board_3d[1][0][0] = -1

    while queue:
        row,column, distance, chance = queue.popleft()

        if row == n - 1 and column == m - 1:
            return distance
        if chance:
            board_one = board_3d[0]
            for i in range(len(dy)):
                n_row = row + dy[i]
                n_column = column + dx[i]

                if not (0 <= n_row < n and 0 <= n_column < m) or board_one[n_row][n_column] == -1:
                    continue

                n_chance = chance
                if board_one[n_row][n_column] == 1:
                    n_chance = False

                board_one[n_row][n_column] = -1
                board_3d[1][n_row][n_column] = -1
                queue.append((n_row, n_column, distance + 1, n_chance))
        else:
            board_one = board_3d[1]
            for i in range(len(dy)):
                n_row = row + dy[i]
                n_column = column + dx[i]

                if not (0 <= n_row < n and 0 <= n_column < m) or board_one[n_row][n_column] == -1 or board_one[n_row][n_column] == 1:
                    continue

                board_one[n_row][n_column] = -1
                queue.append((n_row, n_column, distance + 1, chance))



    return -1

print(solution())