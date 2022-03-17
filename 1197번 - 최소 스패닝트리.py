import sys
import heapq
def find_parent(parents, index):
    if parents[index] != index:
        parents[index] = find_parent(parents, parents[index])

    return parents[index]

def union_parent(parents, one, other):
    one = find_parent(parents, one)
    other = find_parent(parents, other)

    if one < other:
        parents[other] = one
    else:
        parents[one] = other

def get_input():
    input = sys.stdin.readline
    v, e = map(int, input().split())
    edges = []
    for i in range(e):
        # 인덱스 - 1 해주기
        from_node, to_node, price = map(int, input().split())
        heapq.heappush(edges, (price, from_node - 1, to_node - 1))

    return v, edges

def solution(v, edges):
    sum = 0
    parents = [i for i in range(v)]

    while edges:
        price, from_node, to_node = heapq.heappop(edges)
        if find_parent(parents, from_node) != find_parent(parents, to_node):
            union_parent(parents, from_node, to_node)
            sum += price

    return sum

v, edges = get_input()
print(solution(v, edges))
