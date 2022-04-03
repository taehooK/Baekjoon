def solution():
    m = int(input())
    n = int(input())

    check = [False] * (n + 1)
    check[0] = True
    check[1] = True

    for j in range(2, n + 1):
        if check[j]:
            continue
        value = 2
        number = j * value
        while number <= n:
            check[number] = True
            value += 1
            number = j * value

    minNumber = -1
    for number in range(m, n + 1):
        if not check[number]:
            minNumber = number
            break
    if minNumber == -1:
        print(minNumber)
        return

    sum = 0
    for i in range(m, n + 1):
        if not check[i]:
            sum += i
    print(sum)
    print(minNumber)

solution()