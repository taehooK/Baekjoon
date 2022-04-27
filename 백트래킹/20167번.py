def solution():
    n, k = map(int, input().split())
    feeds = list(map(int, input().split()))

    selected = [0] * n
    global ret
    ret = 0
    recursive(feeds, selected, 0, 0, k)

    return ret

def recursive(feeds, selected, index, satisfaction, k):
    global ret
    if index >= len(feeds):
        sum = 0
        temp = 0
        for i in range(len(selected)):
            if selected[i] == 1:
                temp += feeds[i]
                if temp >= k:
                    sum += temp - k
                    temp = 0
        ret = max(ret, sum)
        return

    if satisfaction >= k:#만족도가 k보다 크거나 같은경우
        satisfaction = 0
    if index - 1 < 0 or satisfaction <= 0:  # 이전에 먹지 않았으면
        selected[index] = 0
        recursive(feeds, selected, index + 1, satisfaction, k)
    selected[index] = 1
    satisfaction += feeds[index]
    recursive(feeds, selected, index + 1, satisfaction, k)


print(solution())
