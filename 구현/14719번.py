def get_input():
    h, w = map(int, input().split())
    numbers = list(map(int, input().split()))

    return h, w, numbers

def solution(h, w, numbers):
    ret = 0
    area = [[0 for i in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if h - i <= numbers[j]:
                area[i][j] = 1

    for i in range(len(area)):
        is_facing_wall = False
        count = 0
        for j in range(len(area[0])):
            if area[i][j] == 1:
                is_facing_wall = True
            if is_facing_wall:
                if area[i][j] == 1:
                    ret += count
                    count = 0
                elif area[i][j] == 0:
                    count += 1
    return ret

h, w, numbers = get_input()
print(solution(h, w, numbers))
