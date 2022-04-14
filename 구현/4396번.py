import sys
input = sys.stdin.readline

dy =[-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
def solution():
    n = int(input())

    board = [list(input()) for i in range(n)]
    query = [list(input()) for i in range(n)]

    ret = [['.' for i in range(n)]for i in range(n)]
    is_game_over = False
    for i in range(n):
        for j in range(n):
            if query[i][j] == 'x':
                if board[i][j] == '.':
                    count = 0
                    for k in range(len(dx)):
                        n_row = i + dy[k]
                        n_column = j + dx[k]

                        if not (0 <= n_row < n and 0 <= n_column < n):
                            continue
                        if board[n_row][n_column] == '*':
                            count += 1
                    ret[i][j] = str(count)
                else:
                    is_game_over = True
    if is_game_over:
        for i in range(len(ret)):
            for j in range(len(ret)):
                if board[i][j] == '*':
                    ret[i][j] = '*'

    for char_array in ret:
        print(''.join(char_array))

solution()
