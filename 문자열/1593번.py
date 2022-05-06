def solution():
    target_length, s_length = map(int, input().split())
    target = input()
    string = input()
    ret = 0

    target_map = dict()
    current_map = dict()
    matching_count = 0

    for i in range(len(target)):
        if target[i] not in target_map:
            target_map[target[i]] = 0
        target_map[target[i]] += 1

    for i in range(len(target)):
        if string[i] not in current_map:
            current_map[string[i]] = 0
        current_map[string[i]] += 1
        if string[i] in target_map and current_map[string[i]] <= target_map[string[i]]:
            matching_count += 1
    left = 0
    right = len(target) - 1

    while right < len(string):
        if left > 0:
            removed_char = string[left - 1]
            current_map[removed_char] -= 1

            if removed_char in target_map and current_map[removed_char] < target_map[removed_char]:
                matching_count -= 1

            added_char = string[right]
            if added_char not in current_map:
                current_map[added_char] = 0
            current_map[added_char] += 1

            if added_char in target_map and current_map[added_char] <= target_map[added_char]:
                matching_count += 1

        if len(target) == matching_count:
            ret += 1
        left += 1
        right += 1

    return ret

print(solution())
print(solution())
print(solution())
print(solution())
print(solution())

