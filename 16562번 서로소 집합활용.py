import sys
def find_parent(parents, index):
    if parents[index] != index:
        parents[index] = find_parent(parents, parents[index])

    return parents[index]

def union_parent(parents, prices, one, other):
    one = find_parent(parents, one)
    other = find_parent(parents, other)

    if prices[one] < prices[other]:
        parents[other] = one
    else:
        parents[one] = other

def get_input():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.insert(0, 0)
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        v, w = map(int, input().split())
        graph[v].append(w)

    return n, m, k, graph, prices

def solution(n, m, k, graph, prices):
    # 각각의 head 배열
    parents = [i for i in range(n + 1)]

    group = [] # 각 그룹의 head 번호만 담음
    for i in range(1, n + 1):
        for friend in graph[i]:
            #합쳐져 있지 않으면 합친다.
            if find_parent(parents, i) != find_parent(parents, friend):
                union_parent(parents, prices, i, friend)

    visited = dict()
    sum = 0

    for i in range(1, n + 1):
        parent = find_parent(parents, i)
        if parent not in visited:
            visited[parent] = True
            sum += prices[parent]
    if sum > k:
        print('Oh no')
    else:
        print(sum)

n, m, k, graph, prices = get_input()
solution(n, m, k, graph, prices)

