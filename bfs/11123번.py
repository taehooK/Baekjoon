import sys
from collections import deque
row_offset = [-1, 1, 0, 0]
column_offset = [0, 0, -1, 1]
def solution():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        h , w = map(int, input().split())
        board = []

        for _ in range(h):
            board.append(list(input()))
        count = 0
        queue = deque()
        for i in range(h):
            for j in range(w):
                if board[i][j] == '#':
                    count += 1
                    queue.append((i, j))
                    board[i][j] = '.'

                    while queue:
                        row, column = queue.pop()
                        for k in range(4):
                            n_row = row + row_offset[k]
                            n_column = column + column_offset[k]

                            if not (0 <= n_row < h and 0 <= n_column < w):
                                continue
                            if board[n_row][n_column] == '#':
                                queue.append((n_row, n_column))
                                board[n_row][n_column] = '.'
        print(count)

solution()