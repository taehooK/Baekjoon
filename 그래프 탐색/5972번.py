import heapq
import sys
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    inf = 10e9
    edges = [[] for i in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    hq = []
    visit = [False] * (n + 1)
    distances = [inf] * (n + 1)

    heapq.heappush(hq, (0,1))
    distances[1] = 0

    while hq:
        distance, node = heapq.heappop(hq)
        if visit[node]:
            continue
        visit[node] = True

        for n_node, n_weight in edges[node]:
            n_dist = distance + n_weight
            if distances[n_node] > n_dist:
                distances[n_node] = n_dist
                heapq.heappush(hq, (n_dist, n_node))

    return distances[n]

print(solution())