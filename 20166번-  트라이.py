row_offset = [-1, 1, 0, 0, -1, 1, -1, 1] #상하좌우 대각선왼쪽 위, 대각선 왼쪽 아래, 대각선 오른쪽 위, 대각선 오른쪽 아래
column_offset = [0, 0, -1, 1, -1, -1, 1, 1] #상하좌우 대각선왼쪽 위, 대각선 왼쪽 아래, 대각선 오른쪽 위, 대각선 오른쪽 아래

class trie:
    def __init__(self):
        self.nodes = dict()
        self.count = 0

    def insert(self, string):
        self.__insert_recurisve(string, 0)
    def __insert_recurisve(self, string, index):
        #종료조건
        if index >= len(string):
            self.count += 1
            return
        if string[index] not in self.nodes:
            self.nodes[string[index]] = trie()
        other = self.nodes[string[index]]
        other.__insert_recurisve(string, index + 1)
    def get_count(self, string):
        return self.__get_count(string, 0)

    def __get_count(self, string, index):
        if index >= len(string):
            return self.count
        if string[index] not in self.nodes:
            return -1
        return self.nodes.get(string[index]).__get_count(string, index + 1)

def get_input():
    n, m, k = map(int, input().split())
    board = [[] for i in range(n)]
    target_strings = []
    for i in range(n):
        string = input()
        for j in range(m):
            board[i].append(string[j])
    for i in range(k):
        target_strings.append(input())

    return n, m, k, board, target_strings

def solution(n, m, k, board, target_string):
    trees = [trie() for i in range(k)]
    i = 0
    for string in target_string:
        trees[i].insert(string)
        i += 1

    ret = []
    index = 0
    for string in target_string:
        global count
        count = 0
        for i in range(n):# n번만큼 반복
            for j in range(m):# m번만큼 반복
                dfs(trees[index], board, i, j, board[i][j], len(string))
        ret.append(count)
        index += 1

    for value in ret:
        print(value)

def dfs(tree, board, row, column, string, limit):
    global count
    find = tree.get_count(string)
    if find < 0:
        return
    if len(string) >= limit: #종료조건
        count += 1
        return

    for i in range(len(row_offset)):
        to_row = row + row_offset[i]
        to_column = column + column_offset[i]

        to_row = (len(board) + to_row) % len(board)
        to_column = (len(board[0]) + to_column) % len(board[0])
        dfs(tree, board, to_row, to_column, string + board[to_row][to_column], limit)

n, m, k, board, target_strings = get_input()
solution(n, m, k, board, target_strings)
