def find_parent(parents, index):
    if parents[index] != index:
        parents[index] = find_parent(parents, parents[index])

    return parents[index]

def union_parent(parents, one, other):
    one = find_parent(parents, one)
    other = find_parent(parents, other)

    if one < other:
        parents[other] = one
    else:
        parents[one] = other