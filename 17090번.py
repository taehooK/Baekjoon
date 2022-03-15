def get_input():
    n, m = map(int, input().split())

    field = []
    for i in range(n):
        string = input()
        string_array = []
        for j in range(m):
            string_array.append(string[j])

        field.append(string_array)

    return n, m, field

def solution(n, m, field):
    visited = dict()
    passed = dict()
    answer = 0
    length = n * m

    i = 0
    while i < n and len(visited) < length:
        for j in range(m):#m번만큼 반복
            if (i, j) in visited:
                continue
            count = 0
            row = i
            temp = []
            column = j
            while 0 <= row < n and 0 <= column < m and (row, column) not in visited:
                visited[(row, column)] = True
                temp.append((row, column))
                count += 1

                if field[row][column] == 'U':
                    row -= 1
                elif field[row][column] == 'R':
                    column += 1
                elif field[row][column] == 'D':
                    row += 1
                elif field[row][column] == 'L':
                    column -= 1

            if not (0 <= row < n and 0 <= column < m) or (row, column) in passed : #미로 안에 있지 않거나 빠져나갈수 있는 길이라면
                answer += count
                for other_row, other_column in temp:
                    passed[other_row, other_column] = True
        i += 1

    return answer

n, m, field = get_input()
print(solution(n, m, field))

n, m, field = get_input()
print(solution(n, m, field))

n, m, field = get_input()
print(solution(n, m, field))

n, m, field = get_input()
print(solution(n, m, field))
