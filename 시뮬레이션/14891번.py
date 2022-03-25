def solution():
    n = 4
    gears =[[] for i in range(4)]
    for i in range(n):
        str = input()
        for j in range(8):
            gears[i].append(int(str[j]))

    k = int(input())
    orders = []
    for i in range(k):
        number, rotation = map(int, input().split())
        number -= 1
        orders.append((number, rotation))

    for order in orders:
        rotate_gears = []
        index = order[0]
        rotation = order[1]
        rotate_gears.append((gears[index], rotation))

        #왼쪽 탐색
        if index - 1 >= 0:
            index_temp = index
            change = -1
            while index_temp - 1 >= 0:
                current = gears[index_temp]
                current_9 = current[6]
                left_gear = gears[index_temp - 1]
                left_gear_3 = left_gear[2]
                if current_9 == left_gear_3:
                    break
                rotate_gears.append((left_gear, rotation * change))
                change *= -1
                index_temp -= 1
        if index + 1 < n:
            index_temp = index
            change = -1
            while index_temp + 1 < n:
                current = gears[index_temp]
                current_3 = current[2]
                right_gear = gears[index_temp + 1]
                right_gear_9 = right_gear[6]
                if current_3 == right_gear_9:
                    break
                rotate_gears.append((right_gear, rotation * change))
                change *= -1
                index_temp += 1

        for info in rotate_gears:
            rotate(info[0], info[1])


    sum = 0
    for i in range(n):
        gear = gears[i]
        if gear[0] == 1:
            sum += pow(2, i)

    return sum
def rotate(gear, rotation):
    if rotation == 1: #시계 방향
        last = gear[len(gear) - 1]
        for i in range(len(gear) - 1, 0, -1):
            gear[i] = gear[i - 1]
        #맨 뒤에꺼 저장. 뒤에서 부터 0베이스기준 1번쨰까지 반복
        # i-1을 i에 저장
        gear[0] = last

        # 맨뒤 에꺼를 맨앞에적기
    elif rotation == -1: #반시계 방향
        first = gear[0]
        #첫번째 꺼를 저장, 앞에서 부터 n-1번째까지 반복
        for i in range(len(gear) - 1):
            gear[i] = gear[i + 1]
        # i에 i+1을 저장
        #첫번째꺼를 맨뒤에 적기
        gear[len(gear) - 1] = first

print(solution())

