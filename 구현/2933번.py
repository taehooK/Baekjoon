import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = []
    for _ in range(r):
        string = input().strip()
        board.append(list(string))
    n = int(input())

    attacks = list(map(int, input().split()))
    for i in range(n):
        attack = r - attacks[i]
        start = 0
        end = c - 1
        destroyed = False
        if i % 2 == 0:
            while start <= end:
                if board[attack][start] == 'x':
                    destroyed = True
                    board[attack][start] = '.'
                    break
                start += 1
        else:
            start = c - 1
            end = 0
            while start >= end:
                if board[attack][start] == 'x':
                    destroyed = True
                    board[attack][start] = '.'
                    break
                start -= 1

        if destroyed:
            row, column = attack, start

            for j in range(len(dy)):
                n_row = row + dy[j]
                n_column = column + dx[j]

                if not (0 <= n_row < r and 0 <= n_column < c) or board[n_row][n_column] == '.':
                    continue

                minerals = get_separated_cluster(board, n_row, n_column)
                if minerals is not None:
                    move_sepearted_clusters(board, minerals)
                    break
    print_board(board)


def move_sepearted_clusters(board, minerals):
    min_height = 101
    visited = dict()
    for row, column in minerals:
        visited[(row, column)] = True

    for row, column in minerals:
        i = row + 1
        if board[i][column] == 'x':
            continue
        while i <= len(board):
            if (i, column) in visited:
                break
            if i >= len(board) or board[i][column] == 'x':
                min_height = min(min_height, i - row - 1)
                break
            i += 1

    for row, column in minerals:
        board[row][column] = '.'

    for row, column in minerals:
        n_row = row + min_height
        n_column = column

        board[n_row][n_column] = 'x'


def get_separated_cluster(board, row, column):
    minerals = []
    queue = deque()
    queue.append((row, column))
    visited = dict()
    visited[(row, column)] = True
    while queue:
        row, column = queue.popleft()
        minerals.append((row, column))
        for k in range(len(dy)):
            n_row = row + dy[k]
            n_column = column + dx[k]

            if n_row >= len(board):
                return None
            if not (0 <= n_row < len(board) and 0 <= n_column < len(board[0])) or (n_row, n_column) in visited or \
                    board[n_row][n_column] == '.':
                continue

            queue.append((n_row, n_column))
            visited[(n_row, n_column)] = True

    return minerals


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end='')
        print()
    print()


solution()