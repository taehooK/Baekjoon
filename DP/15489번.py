def solution(r, c, w):
    pascal = [[] for _ in range(30)]

    for i in range(len(pascal)):
        for j in range(0, i + 1):
            pascal[i].append(0)

    pascal[0][0] = 1
    for i in range(1, len(pascal)):
        for j in range(len(pascal[i])):
            if j == 0:
                pascal[i][j] = pascal[i - 1][j]
            elif j == len(pascal[i]) - 1:
                pascal[i][j] = pascal[i - 1][j - 1]
            else:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    row = r - 1
    column = c - 1
    row_count = 0
    sum = 0

    for i in range(row, row + w):
        row_count += 1
        for j in range(column , column + row_count):
            sum += pascal[i][j]

    return sum

r, c, w = map(int, input().split())
print(solution(r, c, w))
