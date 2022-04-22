import sys

input = sys.stdin.readline
def find_parent(parents, index):
    if parents[index] != index:
        parents[index] = find_parent(parents, parents[index])
    return parents[index]

def union_parents(parents, one, other):
    one = find_parent(parents, one)
    other = find_parent(parents, other)
    if one < other:
        parents[other] = one
    else:
        parents[one] = other


def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())
        camps = [list(map(int, input().split())) for _ in range(n)]
        parents = [i for i in range(len(camps))]
        count = len(camps)

        for i in range(n):
            for j in range(i + 1, n):
                distance_squared = (camps[i][0] - camps[j][0]) ** 2 + (camps[i][1] - camps[j][1]) ** 2
                if ((camps[i][2] + camps[j][2]) ** 2 >= distance_squared and
                        find_parent(parents, i) != find_parent(parents, j)):
                    union_parents(parents, i, j)
                    count -= 1
        print(count)


solution()
