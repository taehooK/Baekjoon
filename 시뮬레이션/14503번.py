from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def solution():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    cleaned_area = [[0 for i in range(m)] for i in range(n)]

    queue = deque()
    queue.append((r, c, d))
    cleaned_area[r][c] = 1
    count = 1

    while queue:
        info = queue.popleft()
        y = info[0]
        x = info[1]
        d = info[2]

        nd = d - 1
        if nd < 0:
            nd = len(dy) - 1

        ny = y + dy[nd]
        nx = x + dx[nd]

        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0 and cleaned_area[ny][nx] == 0:
            queue.append((ny, nx, nd))
            cleaned_area[ny][nx] = 1
            count += 1
        else:
            is_free_space = False
            j = 1
            while j <= 3:
                nd -= 1
                if nd < 0:
                    nd = len(dy) - 1
                ny = y + dy[nd]
                nx = x + dx[nd]
                if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0 and cleaned_area[ny][nx] == 0:
                    queue.append((ny, nx, nd))
                    cleaned_area[ny][nx] = 1
                    count += 1
                    is_free_space = True
                    break
                j += 1
            if is_free_space:
                continue
            cur_d = nd
            if nd <= 1: #북동을 남서로
                nd += 2
            else:
                nd -= 2 #남서를 북동으로

            ny = y + dy[nd]
            nx = x + dx[nd]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                queue.append((ny, nx, cur_d))
            else:
                break

    return count
print(solution())





