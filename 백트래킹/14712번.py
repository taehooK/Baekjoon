ret_count = 0

def solution():
    n, m = map(int, input().split())
    board = [[0 for i in range(m)] for j in range(n)]

    global ret_count
    ret_count = 0
    recursive(board, 0, 0)

    return ret_count

def recursive(board, row, column):
    global ret_count

    if row >= len(board):
        ret_count += 1
        return

    if column >= len(board[0]) - 1:
        n_row = row + 1
        n_column = 0
    else:
        n_column = column + 1
        n_row = row
    recursive(board, n_row, n_column)

    if board[row - 1][column] == 0 or board[row - 1][column - 1] == 0 or board[row][column - 1] == 0:
        board[row][column] = 1
        recursive(board, n_row, n_column)
        board[row][column] = 0

print(solution())

