import sys
from collections import deque

def solution():
    input = sys.stdin.readline
    n, m, r = map(int, input().split())

    ret = 0
    direction = dict()

    direction['E'] = (0, 1)
    direction['N'] = (-1, 0)
    direction['S'] = (1, 0)
    direction['W'] = (0, -1)
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    for _ in range(r):
        string = input().split()
        row_atk, col_atk, d = int(string[0]) - 1, int(string[1]) - 1, string[2]
        row_df, col_df = map(int, input().split())
        row_df -= 1
        col_df -= 1

        if board[row_atk][col_atk] > 0:
            queue = deque()
            queue.append((row_atk, col_atk, board[row_atk][col_atk]))
            board[row_atk][col_atk] *= -1
            ret += 1

            while queue:
                row_atk, col_atk, length = queue.popleft()
                row_atk += direction[d][0]
                col_atk += direction[d][1]

                i = 1
                while i <= length - 1 and 0 <= row_atk < n and 0 <= col_atk < m:
                    if board[row_atk][col_atk] > 0:
                        queue.append((row_atk, col_atk, board[row_atk][col_atk]))
                        board[row_atk][col_atk] *= -1
                        ret += 1

                    row_atk += direction[d][0]
                    col_atk += direction[d][1]
                    i += 1

        if board[row_df][col_df] < 0:
            board[row_df][col_df] *= -1

    print(ret)
    for i in range(n):
        for j in range(m):
            if board[i][j] < 0:
                print("F", end=" ")
            else:
                print("S", end=" ")
        print()

solution()