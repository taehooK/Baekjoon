def recursive(index, sum):
    global count
    if sum > n:
        return
    elif sum == n:
        count += 1
        if count == k:
            print("+".join(map(str, array[:index])))
        return

    for i in [1, 2, 3]:
        array[index] = i
        sum += array[index]
        recursive(index + 1, sum)
        sum -= array[index]


n, k = map(int, input().split())
array = [0] * 10
count = 0

recursive(0, 0)
if count < k:
    print(-1)



