import sys
limit_number = 10000000
sys.setrecursionlimit(limit_number)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_dict = dict()

for i in range(len(in_order)):
    in_order_dict[in_order[i]] = i

def recursive(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return

    pivot = in_order_dict[post_order[post_right]]
    left_size = pivot - in_left

    print(in_order[pivot], end=' ')
    recursive(in_left, pivot - 1, post_left, post_left + left_size - 1)
    recursive(pivot + 1, in_right, post_left + left_size, post_right - 1)


recursive(0, len(in_order) - 1, 0, len(post_order) - 1)


