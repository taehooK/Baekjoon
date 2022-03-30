import sys
from copy import deepcopy
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution():
    input = sys.stdin.readline
    n , m = map(int, input().split())

    board = [list(map(int, input().strip())) for i in range(n)]
    board[0][0] = -1

    board_3d = [[array[:] for array in board], [array[:] for array in board]]
    if n == 1 and m == 1:
        return 1
    queue = deque()
    queue.append((board, 0, 0, 1, True))

    #board복사를
    while queue:
        board, row,column,distance, has_skill = queue.popleft()

        if row == n - 1 and column == m - 1:
            return distance

        for i in range(len(dy)):
            n_row = row + dy[i]
            n_column = column + dx[i]

            if not (0 <= n_row < n and 0 <= n_column < m) or board[n_row][n_column] == -1:
                continue

            if board[n_row][n_column] == 0:
                board[n_row][n_column] = -1
                queue.append((board, n_row, n_column, distance + 1, has_skill))
            elif board[n_row][n_column] == 1 and has_skill:
                copy_board = [array[:] for array in board]
                copy_board[n_row][n_column] = -1
                queue.append((copy_board, n_row, n_column, distance + 1, False))


    return -1

print(solution())


