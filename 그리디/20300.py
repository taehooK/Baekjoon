def solution():
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    first = 0
    last = n - 1
    max_loss = 0;

    if n % 2 == 1:
        max_loss = array[last]
        last -= 1

    while first < last:
        sum_loss = array[first] + array[last]
        max_loss = max(sum_loss, max_loss)
        first += 1
        last -= 1

    return max_loss

print(solution())
