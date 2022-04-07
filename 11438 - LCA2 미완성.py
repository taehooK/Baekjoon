import sys

def get_input():
    input = sys.stdin.readline
    n = int(input())
    edges = [[] for i in range(n + 1)] # 1 베이스
    for j in range(1, n):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    m = int(input())
    target = [tuple(map(int, input().split())) for i in range(m)]

    return n, m, edges, target

#노드들의 깊이를담는 배열
n, m, edges, target = get_input()
parents = [[0] * (n + 1) for i in range(n + 1)]#노드들의 부모노드들을 담는 배열
depths = [0 for i in range(n + 1)]

def set_parents(root):
    visited = dict()
    dfs(1, visited, 0)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1] #

def dfs(node, visited, depth):
    visited[node] = True
    depth[node] = depth

    for neighbor in edges[node]:
        if neighbor not in visited:
            parents[neighbor][0] = node
            dfs(neighbor, visited, depth)
def solution():








