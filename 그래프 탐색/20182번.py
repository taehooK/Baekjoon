import heapq
import sys

input = sys.stdin.readline
def solution():
    n, m, a, b, c = map(int, input().split())
    edges = [[] for i in range(n + 1)]

    for _ in range(m):
        one, other, price = map(int, input().split())
        edges[one].append((other, price))
        edges[other].append((one, price))

    left = 1
    right = 20
    ret = -1

    while left <= right:
        middle = (left + right) // 2
        if dijkstra(edges, a, b, middle, c):
            ret = middle
            right = middle - 1
        else:
            left = middle + 1

    return ret


def dijkstra(edges, start, end, k, total_money):
    INF = 10e7
    distances = [INF] * len(edges)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        distance, node = heapq.heappop(queue)
        if distance > distances[node] or distance > total_money:
            continue
        if node == end:
            return True

        for neighbor_node, price in edges[node]:
            new_distance = distance + price
            if price <= k and new_distance < distances[neighbor_node]:
                distances[neighbor_node] = new_distance
                heapq.heappush(queue, (new_distance, neighbor_node))

    return False

print(solution())
























