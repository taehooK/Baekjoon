from collections import deque

def solution():
    answer = []
    expression = input()
    queue = deque()
    brackets = []

    for i in range(len(expression)):
        if expression[i] == '(':
            queue.append(i)
        elif expression[i] == ')':
            left = queue.pop()
            brackets.append((left, i))

    valids = [True] * len(expression)
    visited = dict()
    solution_recursive(expression, 0, valids, visited, brackets, answer)
    answer = answer[1:] # 괄호 제거가 한개도 안된 수식 제거
    answer.sort()

    for string in answer:
        print(string)
def solution_recursive(expression, index, valids, visited, brackets, answer):
    #종료 조건
    #index가 brackets범위를 벗어남
    if index >= len(brackets):
        temp =''
        for j in range(len(expression)):
            if valids[j]:
                temp += expression[j]
        if temp not in visited:
            answer.append(temp)
            visited[temp] = True
        return
    solution_recursive(expression, index + 1, valids,visited, brackets, answer)
    valids[brackets[index][0]] = False
    valids[brackets[index][1]] = False
    solution_recursive(expression, index + 1, valids,visited, brackets, answer)
    valids[brackets[index][0]] = True
    valids[brackets[index][1]] = True

solution()















