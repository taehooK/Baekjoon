ret_count = 0
def solution():
    n, k = map(int, input().split())
    kits = list(map(int, input().split()))

    used = [0] * n
    global ret_count
    ret_count = 0
    recursive(n, k, kits, 500, used, 0)
    print(ret_count)

def recursive(n, k, kits, weight, used, count):
    global ret_count
    if count >= n:
        ret_count += 1
        return

    weight -= k
    for i in range(len(kits)):
        if used[i] == 0:
            weight += kits[i]
            if weight >= 500:
                used[i] = 1
                recursive(n, k, kits, weight, used, count + 1)
                used[i] = 0
            weight -= kits[i]

solution()
