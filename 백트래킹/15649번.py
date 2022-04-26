def solution():
    n, m = map(int, input().split())
    array = [0] * m
    used = [0] * (n + 1)
    recursive(array, used, 0, n)

def recursive(array, used, index, n):
    if index >= len(array):
        for number in array:
            print(number, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if used[i] == 0:
            array[index] = i
            used[i] = 1
            recursive(array, used, index + 1, n)
            used[i] = 0

solution()



