import sys
input = sys.stdin.readline
def solution():
    n = int(input())

    coordinates = [list(map(int, input().split())) for _ in range(n)]

    sum = 0
    for i in range(len(coordinates)):
        if i + 1 < len(coordinates):
            sum += (coordinates[i][0] + coordinates[i + 1][0]) * (coordinates[i][1] - coordinates[i + 1][1])
        else:
            sum += (coordinates[i][0] + coordinates[0][0]) * (coordinates[i][1] - coordinates[0][1])

    sum = abs(sum) / 2
    sum = round(sum, 1)

    return sum

print(solution())
print(solution())
print(solution())
print(solution())



