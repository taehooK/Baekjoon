from collections import deque

row_offset = [0, 0, -1, 1]
column_offset = [1, -1, 0, 0]

def get_input():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    pieces = []
    for i in range(k):
        row, column, move = map(int, input().split())
        pieces.append([row - 1, column - 1, move - 1, 1])

    return n, k, board, pieces

def move(board, piece, board_pieces):
    row = piece[0]
    column = piece[1]
    move = piece[2]
    from_level = piece[3]
    to_row = row + row_offset[move]
    to_column = column + column_offset[move]

    if not (0 <= to_row < len(board) and 0 <= to_column < len(board)) or board[to_row][to_column] == 2:
        if row_offset[move] != 0:
            temp = row_offset[move] * -1
            move = row_offset.index(temp)
        else:
            temp = column_offset[move] * -1
            move = column_offset.index(temp)
        piece[2] = move
        to_row = row + row_offset[move]
        to_column = column + column_offset[move]

    if 0 <= to_row < len(board) and 0 <= to_column < len(board) and board[to_row][to_column] < 2:
        piece_queue_temp = deque()
        from_board_pieces = board_pieces[row][column]
        to_board_pieces = board_pieces[to_row][to_column]

        to_level = len(to_board_pieces) + 1
        i = 0
        pop_count = len(from_board_pieces) - (from_level - 1)

        while i < pop_count:
            piece_temp = from_board_pieces.pop()
            piece_queue_temp.appendleft(piece_temp)
            i += 1

        while piece_queue_temp:
            piece_temp = 0
            if board[to_row][to_column] == 0:
                piece_temp = piece_queue_temp.popleft()
            elif board[to_row][to_column] == 1:
                piece_temp = piece_queue_temp.pop()
            else:
                print('error')
            piece_temp[0] = to_row
            piece_temp[1] = to_column
            piece_temp[3] = to_level
            to_board_pieces.append(piece_temp)
            to_level += 1
    else:
        return row, column

    return to_row, to_column

def solution(n, board, pieces):
    board_pieces = [[deque() for i in range(n)] for j in range(n)]
    for piece in pieces:
        board_pieces[piece[0]][piece[1]].append(piece)

    for turn in range(1, 1001):
        for piece in pieces:
            row, column = move(board, piece, board_pieces)
            if len(board_pieces[row][column]) >= 4:
                return turn

    return -1

n, k, board, pieces = get_input()
print(solution(n, board, pieces))


'''
def pirnt_board_pieces_count(board_pieces):
    for i in range(len(board_pieces)):
        for j in range(len(board_pieces)):
            print(len(board_pieces[i][j]), end=' ')

        print()
    print()
'''

