from collections import deque

def solution():
    n = 3
    board = [list(map(int, input().split())) for i in range(n)]

    target_board = [[0 for i in range(n)] for _ in range(n)]
    number = 1
    for i in range(n):
        for j in range(n):
            target_board[i][j] = number
            number += 1

    target_board[n - 1][n - 1] = 0
    queue = deque()
    queue.append((board, 0))

    while deque():
        if 
