import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        array = list(map(int, input().split()))
        for j in range(1, len(array) - 1):
            pre = array[j] - 1
            next = array[j + 1] - 1
            graph[pre].append(next)
    return n, m, graph

def solution(n, m, graph):
    degrees = [0] * n  #진입 차수 배열 리셋
    queue = deque()
    ret = []

    for i in range(n):
        for j in range(len(graph[i])):
            degrees[graph[i][j]] += 1

    # 차수가 0인것 넣기
    for i in range(n):
        if degrees[i] == 0:
            queue.append(i)

    #큐가 빌때까지 반복
    while queue:
        index = queue.popleft()
        ret.append(index)
        for next in graph[index]:
            degrees[next] -= 1
            if degrees[next] == 0:
                queue.append(next)
    if len(ret) < n:#진입차수가 0보다 큰게 있으면 0출력
        print('0')
    else:
        for index in ret:
            print(index + 1)


n, m,graph = get_input()
solution(n, m, graph)