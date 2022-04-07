def solution(n, m, numbers, queries):
    answer = []

    for start, end in queries:
        start -= 1
        end -= 1
        while start <= end and numbers[start] == numbers[end]:
            start += 1
            end -= 1
        value = 0
        if start > end:
            value = 1
        answer.append(value)

    for value in answer:
        print(value)

def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    queries = [tuple(map(int, input().split())) for i in range(m)]
    return n, m, numbers, queries

n, m, numbers, queries = get_input()
solution(n, m, numbers, queries)


