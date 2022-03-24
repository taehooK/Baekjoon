import sys
import heapq
def solution():
    input = sys.stdin.readline
    n = int(input())
    children = [[] for _ in range(n + 1)]

    for i in range(n - 1):
        parent, child, cost = map(int, input().split())
        children[parent].append((child, cost))

    max_child_edge = [0] * (n + 1)
    max_tree_width = 0

    for i in range(n, 0, -1):
        child_cost_heapq = []
        for child in children[i]:
            heapq.heappush(child_cost_heapq, -(child[1] + max_child_edge[child[0]])) # -처리해준거 주의

        if child_cost_heapq:
            max_child_edge[i] = -child_cost_heapq[0]

        count = 0
        width = 0
        while child_cost_heapq:
            if count >= 2:
                break
            width += -(heapq.heappop(child_cost_heapq))
            count += 1
        max_tree_width = max(max_tree_width, width)

    return max_tree_width

print(solution())


