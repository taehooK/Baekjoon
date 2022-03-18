import sys
input = sys.stdin.readline
limit_number = 15000000
sys.setrecursionlimit(limit_number)
def get_depth(parents, index, depth):
    # 종료조건 - 부모노드일 때
    if parents[index] == index:
        return depth
    return get_depth(parents, parents[index], depth + 1)

def solution(n, edges, target_node):
    parents = [i for i in range(n + 1)]
    # paretns 초기화
    for i in range(1, n + 1):
        for child in edges[i]:
            parents[child] = i
    if target_node[0] == target_node[1]:
        return target_node[0]
    parent_node_one = parents[target_node[0]]
    parent_node_other = parents[target_node[1]]

    one_depth = get_depth(parents, parent_node_one, 1)
    other_depth = get_depth(parents, parent_node_other, 1)
    if one_depth < other_depth:
        parent_node_one = target_node[0]
    elif one_depth > other_depth:
        parent_node_other = target_node[1]

    while parent_node_one != parent_node_other:
        if one_depth > other_depth:
            parent_node_one = parents[parent_node_one]
            one_depth -= 1
        else:
            parent_node_other = parents[parent_node_other]
            other_depth -= 1

    return parent_node_one

def get_input():
    n = int(input())
    edges = [[] for i in range(n + 1)] # 1 베이스
    for j in range(1, n):
        u, v = map(int, input().split())
        edges[u].append(v)
    target = tuple(map(int, input().split()))

    return n, edges, target

t = int(input())
for i in range(t):
    n, edges, target = get_input()
    print(solution(n, edges, target))



