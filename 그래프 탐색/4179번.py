import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]
    queue = deque()

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'J':
                queue.appendleft((i, j, 0))
            elif board[i][j] == 'F':
                queue.append((i, j, -1))

    while queue:
        row, column, distance = queue.popleft()
        if board[row][column] == 'J':
            if row == 0 or row == r - 1 or column == 0 or column == c - 1:
               return distance + 1
            for i in range(len(dy)):
                ny = row + dy[i]
                nx = column + dx[i]
                if board[ny][nx] == '.':
                    queue.append((ny, nx, distance + 1))
                    board[ny][nx] = board[row][column]
        else:
            for i in range(len(dy)):
                ny = row + dy[i]
                nx = column + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if board[ny][nx] == '.' or board[ny][nx] == 'J':
                        queue.append((ny, nx, -1))
                        board[ny][nx] = board[row][column]

    return "IMPOSSIBLE"

print(solution())


    #F면 상하 좌우 번지기 (벽이나 불이 아닌 경우에만)
    #면 상하 좌우 이동(불이나 벽이나 방문했던데가 아닌경우에만)
    #J고 벽에 가장자리이면 출력

