
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

cctv_d = [[0], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [1, 3], [1, 2], [0, 2]], [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]], [[0, 1, 2, 3]]]
min_cnt = 0
zero_cnt = 0

def solution():
    n, m = map(int, input().split())

    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    global min_cnt
    global zero_cnt
    zero_cnt = 0
    min_cnt = 100000

    cctv_list = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                zero_cnt += 1
            elif 0 < board[i][j] < 6:
                cctv_list.append([board[i][j], i, j, 0]) # cctv번호, row, column, 회전인덱스

    recursive(board, cctv_list, 0)

    return min_cnt

def spread(board, cctv, value):
    for d in cctv_d[cctv[0]][cctv[3]]:
        n_row = cctv[1] + dy[d]
        n_column = cctv[2] + dx[d]

        while 0 <= n_row < len(board) and 0 <= n_column < len(board[0]) and board[n_row][n_column] != 6:
            if board[n_row][n_column] <= 0:
                board[n_row][n_column] += value
            n_row += dy[d]
            n_column += dx[d]

def recursive(board, cctv_list, cctv_index):
    global min_cnt

    if cctv_index >= len(cctv_list):
        count = 0
        for cctv in cctv_list:
            for d in cctv_d[cctv[0]][cctv[3]]:
                n_row = cctv[1] + dy[d]
                n_column = cctv[2] + dx[d]

                while 0 <= n_row < len(board) and 0 <= n_column < len(board[0]) and board[n_row][n_column] != 6:
                    if board[n_row][n_column] == 0:
                        board[n_row][n_column] = '#'
                        count += 1
                    n_row += dy[d]
                    n_column += dx[d]

        count = zero_cnt - count
        if count < min_cnt:
            min_cnt = count

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 0
        return
    cctv = cctv_list[cctv_index]
    for i in range(len(cctv_d[cctv[0]])):
        cctv[3] = i
        recursive(board, cctv_list, cctv_index + 1)

print(solution())




