import math
def solution(x1, y1, r1, x2, y2, r2):
    #두 원이 두 점에서 만나는 경우
    distance = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    answer = -1
    if x1 == x2 and y1 == y2 and r1 == r2:
        answer = -1
    elif r1 + r2 > distance and abs(r1 - r2) < distance:
        answer = 2
    elif r1 + r2 == distance or abs(r1 - r2) == distance: #두 원이 한 점에서 만나는 경우, 내접, 외접
        answer = 1
    elif r1 + r2 < distance or abs(r1 - r2) > distance:
        answer = 0
    return answer

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution(x1, y1, r1, x2, y2, r2))

