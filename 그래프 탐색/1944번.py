import sys
import heapq
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def find_parent(parents, row, column):
    if parents[(row, column)] != (row, column):
        n_row, n_column = parents[(row, column)]
        parents[(row, column)] = find_parent(parents, n_row, n_column)
    return parents[(row, column)]


def union_parents(parents, one_row, one_column, other_row, other_column):
    one_row, one_column = find_parent(parents, one_row, one_column)
    other_row, other_column = find_parent(parents, other_row, other_column)

    if (one_row, one_column) < (other_row, other_column):
        parents[(other_row, other_column)] = (one_row, one_column)
    else:
        parents[(one_row, one_column)] = (other_row, other_column)


def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    edges = []
    nodes = []
    # 1. 노드 위치 찾기
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 'S' or board[i][j] == 'K':
                nodes.append((i, j))
    for node in nodes:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        queue = deque()
        queue.append((0, node[0], node[1]))
        visited[node[0]][node[1]] = 1
        count = 0
        while queue:
            distance, row, column = queue.popleft()

            for i in range(len(dy)):
                n_row = row + dy[i]
                n_column = column + dx[i]
                # 벽이 아니면
                if board[n_row][n_column] != '1' and visited[n_row][n_column] == 0:
                    queue.append((distance + 1, n_row, n_column))
                    visited[n_row][n_column] = 1
                    if board[n_row][n_column] == 'K' or board[n_row][n_column] == 'S':
                        # 이미 존재하는 거리가 아니면
                        heapq.heappush(edges, (distance + 1, node[0], node[1], n_row, n_column))
                        count += 1
            if count >= len(nodes) - 1:
                break

    parents = dict()
    for row, column in nodes:
        parents[(row, column)] = (row, column)

    ret_distance = 0
    count = 0
    while edges:
        distance, f_row, f_column, t_row, t_column = heapq.heappop(edges)
        if find_parent(parents, f_row, f_column) != find_parent(parents, t_row, t_column):
            union_parents(parents, f_row, f_column, t_row, t_column)
            ret_distance += distance
            count += 1

        if count >= len(nodes) - 1:
            break

    if count < len(nodes) - 1:
        return -1

    return ret_distance

print(solution())
