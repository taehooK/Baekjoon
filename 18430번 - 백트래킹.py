shape = [[(0, -1), (1, 0)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]

def get_input():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    return n, m, board

def solution(n, m, board):
    global max_sum
    max_sum = 0
    visited = [[False for i in range(m)] for j in range(n)]

    dfs(board, 0, 0, visited, 0)
    return max_sum

def dfs(board, row, column, visited, sum):
    global max_sum
    if column >= len(board[0]):
        row += 1
        column = 0

    if row >= len(board):
        if sum > max_sum:
            max_sum = sum
        return
    if not visited[row][column]:
        for k in range(len(shape)):
            first_row = row + shape[k][0][0]
            first_column = column + shape[k][0][1]
            second_row = row + shape[k][1][0]
            second_column = column + shape[k][1][1]

            if (0 <= first_row < len(board) and
                    0 <= first_column < len(board[0]) and
                    0 <= second_row < len(board) and
                    0 <= second_column < len(board[0]) and
                    not visited[first_row][first_column] and
                    not visited[second_row][second_column]):
                value = board[row][column] * 2 + board[first_row][first_column] + board[second_row][second_column]
                visited[row][column] = True
                visited[first_row][first_column] = True
                visited[second_row][second_column] = True
                dfs(board, row, column + 1, visited, sum + value)
                visited[row][column] = False
                visited[first_row][first_column] = False
                visited[second_row][second_column] = False

    dfs(board, row, column + 1, visited, sum)


n, m, board = get_input()
print(solution(n, m, board))
