import sys
input = sys.stdin.readline
ret = 0
def solution():
    INF = 10000000
    n, m, a, b, c = map(int, input().split())
    edges = [[] for i in range(n+ 1)]
    for _ in range(m):
        from_n, to_n, price = map(int, input().split())

        edges[from_n].append((to_n, price))
        edges[to_n].append((from_n, price))

    global ret
    ret = INF

    visited = dict()
    visited[a] = 1
    recursive(visited, edges, c, 0, a, b)

    if ret == INF:
        ret = -1
    return ret

def recursive(visited, edges, remain_money, max_value, current, target):
    global ret
    #종료조건
    if current == target:
        ret = min(ret, max_value)
    #수행문
    for edge in edges[current]:
        neighbor = edge[0]
        price = edge[1]
        # 방문하지 않은 곳이면서 남은돈으로 갈 수 있으면
        if neighbor not in visited and remain_money >= price:
            new_visited = visited.copy()
            new_visited[neighbor] = 1
            recursive(new_visited, edges, remain_money - price, max(max_value, price), neighbor, target)
        # visited 새로 복사 후 삽입, remain_money 감소, max_value 갱신, current갱신

print(solution())













