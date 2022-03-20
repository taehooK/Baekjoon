global min_count
global max_count
def solution(number):
    global min_count
    global max_count
    min_count = 10000
    max_count = 0
    dfs(number, 0)

    print(min_count, max_count)

def separate_number(number, one, two):
    ret = [0, 0 ,0]
    section = [0, one, two]
    digit = get_digit(number)
    ret_index = len(ret) - 1
    iterator = digit

    for i in range(len(section) - 1, -1, -1):
        limit = section[i]
        digit = 1
        while iterator > limit:
            remainder = number % 10
            number //= 10
            ret[ret_index] += remainder * digit
            digit *= 10
            iterator -= 1
        ret_index -= 1

    return ret

def get_digit(number):
    digit = 0
    while number > 0:
        digit += 1
        number //= 10
    return digit

def get_odd_count(number):
    count = 0
    while number > 0:
        remainder = number % 10
        if remainder % 2 == 1:
            count += 1
        number //= 10
    return count

def dfs(number, count):
    global max_count
    global min_count
    count += get_odd_count(number)
    digit = get_digit(number)

    if digit == 1:
        min_count = min(min_count, count)
        max_count = max(max_count, count)
    elif digit == 2:
        dfs(number // 10 + number % 10, count)
    else:
        one = 1
        while one <= digit - 2:
            two = one + 1
            while two <= digit - 1:
                numbers = separate_number(number, one, two)
                sum = 0
                for num in numbers:
                    sum += num
                dfs(sum, count)
                two += 1
            one += 1

n = int(input())
solution(n)





