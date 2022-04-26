def is_correct():
    for query in queries:
        strike = 0
        ball = 0
        for i in range(len(array)):
            if array[i] == query[0][i]:
                strike += 1
            elif array[i] in query[0]:
                ball += 1
        if strike != int(query[1]) or ball != int(query[2]):
            return False
    return True


def recursive(index):
    global ret_count
    if index >= len(array):
        if is_correct():
            ret_count += 1
        return

    for i in range(1, 10):
        array[index] = str(i)
        j = index - 1
        while j >= 0 and array[index] != array[j]:
            j -= 1

        if j < 0:
            recursive(index + 1)

n = int(input())
ret_count = 0
array = ['0'] * 3
queries = [tuple(map(str, input().split())) for i in range(n)]
recursive(0)
print(ret_count)




