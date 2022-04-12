import heapq

def solution():
    n = int(input())
    q = []
    heapq.heappush(q, 4)

    for i in range(2, n + 1):
        life = 3
        if i % 2 == 0:
            life = 4
        for _ in range(len(q)):
            heapq.heappush(q, i + life)

        while q[0] <= i:
            heapq.heappop(q)

    return len(q)

print(solution())