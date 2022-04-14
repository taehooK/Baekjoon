import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def solution():
    n, m, k = map(int, input().split())

    board = [list(input().strip()) for _ in range(n)]
    board = [[board[i][:] for i in range(n)] for _ in range(k + 1)]

    queue = deque() # row, column, 벽부순횟수, 거리
    queue.append((0, 0, 0, 1))
    for j in range(k + 1):
        board[j][0][0] = -1
    target_n = n - 1
    target_m = m - 1

    while queue:
        row, column, d_cnt, distance = queue.popleft()# 꺼내기
        # 종료조건 row = n - 1, column = m - 1
        if row == target_n and column == target_m:
            return distance
        n_distance = distance + 1
        # 수행문
        for i in range(len(dy)):
            n_row = row + dy[i]
            n_column = column + dx[i]
            if 0 <= n_row < n and 0 <= n_column < m:
                if board[d_cnt][n_row][n_column] == '1' and d_cnt < k:
                    queue.append((n_row, n_column, d_cnt + 1, n_distance))
                    board[d_cnt][n_row][n_column] = -1
                    board[d_cnt + 1][n_row][n_column] = -1
                elif board[d_cnt][n_row][n_column] == '0':
                    queue.append((n_row, n_column, d_cnt, n_distance))
                    board[d_cnt][n_row][n_column] = -1

    return -1
print(solution())

