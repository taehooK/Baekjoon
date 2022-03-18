import copy
shape = [[(0, -1), (1, 0)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]

def get_input():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    return n, m, board

def solution(n, m, board):
    global max_sum
    max_sum = 0
    dp = [0] * 9
    dfs(board, 0, 0, dp)

    return max_sum

def dfs(board, sum, count, dp):
    global max_sum
    if sum > max_sum:
        max_sum = sum
    if sum > dp[count]
    dp[count] = sum
    #종료 조건 for문으로 끝까지 반복시
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1:
                for k in range(len(shape)):
                    first_row = i + shape[k][0][0]
                    first_column = j + shape[k][0][1]
                    second_row = i + shape[k][1][0]
                    second_column = j + shape[k][1][1]

                    if (0 <= first_row < len(board) and
                    0 <= first_column < len(board[0]) and
                    0 <= second_row < len(board) and
                    0 <= second_column < len(board[0]) and
                    board[first_row][first_column] != -1 and
                    board[second_row][second_column] != -1):
                        value = board[i][j] * 2 + board[first_row][first_column] + board[second_row][second_column]
                        temp_board = copy.deepcopy(board)
                        temp_board[i][j] = -1
                        temp_board[first_row][first_column] = - 1
                        temp_board[second_row][second_column] = - 1
                        if dp[count] > sum + value:
                            continue
                        dfs(temp_board, sum + value, count + 1, dp)

n, m, board = get_input()
print(solution(n, m, board))
