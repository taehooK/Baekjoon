import sys
limit_number = 15000000
sys.setrecursionlimit(limit_number)
class tree_node:
    def __init__(self, distance):
        self.distance = distance
        self.nodes = []
    def insert(self, node):
        self.nodes.append(node)

def set_tree(graph, r):
    node = tree_node(0)
    node_index = r
    visited = dict()
    visited[node_index] = True
    set_tree_recursive(graph, visited, node, node_index)

    return node

def set_tree_recursive(graph, visited, parent_node, node_index):
    for neighbor in graph[node_index]:
        to_node = neighbor[0]
        if to_node not in visited:
            visited[to_node] = True
            distance = neighbor[1]

            node = tree_node(distance)
            parent_node.insert(node)
            set_tree_recursive(graph, visited, node, to_node)

def get_input():
    input = sys.stdin.readline
    n, r = map(int, input().split())
    graph =[[] for i in range(n)]
    # 인덱스 - 1 주의
    for i in range(n - 1):
        from_node, to_node, distance = map(int, input().split())
        from_node -= 1
        to_node -= 1
        graph[from_node].append((to_node, distance))
        graph[to_node].append((from_node, distance))

    return n, r, graph

def get_max_distance(node):
    return get_max_distance_recursive(node, 0)

def get_max_distance_recursive(node, distance):
    max_distance = 0
    for child in node.nodes:
        temp = get_max_distance_recursive(child, child.distance)
        max_distance = max(max_distance, temp)
    return distance + max_distance

def solution(n, r, graph):
    r -= 1
    root = set_tree(graph, r)

    giga_distance = 0
    node = root
    while len(node.nodes) == 1:
        giga_distance += node.distance
        node = node.nodes[0]
    giga_distance += node.distance

    giga_to_long_distance = get_max_distance(node)

    print(giga_distance, end=' ')
    print(giga_to_long_distance)

n, r, graph = get_input()
solution(n, r, graph)
