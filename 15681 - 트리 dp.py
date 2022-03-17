import sys
limit_number = 15000000
sys.setrecursionlimit(limit_number)
class node:
    def __init__(self, number):
        self.number = number
        self.nodes = []
    def insert(self, node):
        self.nodes.append(node)

def get_input():
    input = sys.stdin.readline
    n, r, q = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    for i in range(1, n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    queries = []
    for i in range(q):
        queries.append(int(input()))

    return n, r, q, graph, queries

def tree_set(graph, start_index):

    root = node(start_index)
    visited = dict()
    visited[start_index] = True

    tree_set_recurisve(graph, visited, root, start_index)

    return root

def tree_set_recurisve(graph, visited, parent_node, index):
    # 종료조건 - 모든 이웃노드 탐색
    for child_index in graph[index]:
        #방문하지 않았으면
        if child_index not in visited:
            visited[child_index] = True
            child_node = node(child_index)
            parent_node.insert(child_node)
            tree_set_recurisve(graph, visited, child_node, child_index)

def get_dp_tree(root, dp):
    #dfs진행
    get_dp_tree_recursive(root, dp)

def get_dp_tree_recursive(node, dp):
    #종료 조건 - dp에 적혀있거나, 모든 하위노드를 탐색했거나
    count = 1
    for child in node.nodes:
        if dp[child.number] == 0:
            get_dp_tree_recursive(child, dp)
        count += dp[child.number]
    dp[node.number] = count


def solution(n, r, q, graph, queries):
    root = tree_set(graph, r)# 트리 연결, r 부터 시작

    dp = [0 for i in range(n + 1)]

    get_dp_tree(root, dp)

    for query in queries:# 쿼리의 개수만큼 반복
        print(dp[query])

n, r, q, graph, queries = get_input()
solution(n, r, q, graph, queries)
