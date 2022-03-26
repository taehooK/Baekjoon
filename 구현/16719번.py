
def recursive(visited, string, left, right):
    min_char = 'a'
    min_index = -1

    i = left
    while i <= right:
        if i not in visited and min_char > string[i]:
            min_char = string[i]
            min_index = i
        i +=1

    if min_char == 'a':
        return
    visited[min_index] = True
    for i in range(len(string)):
        if i in visited:
            print(string[i], end='')
    print()
    recursive(visited, string, min_index + 1, right)
    recursive(visited, string, left, min_index - 1)

def solution(string):
    visitied = dict()
    recursive(visitied, string, 0, len(string) - 1)


string = input()
solution(string)



