import sys
def get_input():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dp = [0] * n
    graph = [[] for i in range(n)]
    for i in range(m):
        pre_index, index = map(int, input().split())
        graph[pre_index - 1].append(index - 1)
        dp[index - 1] += 1

    return graph, dp

def solution(graph, dp):
    # 이수한 과목의 수가 n보다 작을동안반복
    ret = [0] * len(graph)
    n = len(graph)
    term = 0
    count = 0
    while count < n:
        term += 1
        complete = []
        for i in range(len(graph)):
            if dp[i] == 0:
                ret[i] = term
                count += 1
                complete.append(i)
        for subject in complete:
            for index in graph[subject]:
                dp[index] -= 1
            dp[subject] -= 1


    for term in ret:
        print(term, end=' ')

graph, dp = get_input()
solution(graph, dp)