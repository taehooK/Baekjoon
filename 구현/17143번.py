import sys
class Shark:
    def __init__(self, row, column, speed, size, direction):
        self.row = row
        self.column = column
        self.speed = speed
        self.size = size
        self.direction = direction

    def reverse_direction(self):
        if self.direction == 0 or self.direction == 2:
            self.direction += 1
        elif self.direction == 1 or self.direction == 3:
            self.direction -= 1

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def solution():
    input = sys.stdin.readline
    r, c, m = map(int, input().split())
    sharks = []
    board = [[None for i in range(c)] for _ in range(r)]

    for _ in range(m):
        row, column, speed, direction, size = map(int , input().split())
        shark = Shark(row - 1, column - 1, speed, size, direction - 1)
        board[shark.row][shark.column] = shark
        sharks.append(shark)

    ret = 0
    for j in range(c):
        #i번째 열에서 제일 위에있는 상어찾기
        eat_shark = None
        for i in range(r):
            if board[i][j] is not None:
                eat_shark = board[i][j]
                break
        if eat_shark is not None:
            ret += eat_shark.size # 크기 누적
            sharks.remove(eat_shark) # 상어들에서 없애기
        n_board = [[None for i in range(c)] for _ in range(r)]
        remove_sharks = []
        # 상어 이동
        for shark in sharks:
            #스피드만큼 반복
            direction = shark.direction
            n_row = shark.row + (dy[direction] * shark.speed)
            n_column = shark.column + (dx[direction] * shark.speed)

            if n_row < 0:
                n_row = -((-n_row) % ((r - 1) * 2))
            else:
                n_row = n_row % ((r - 1) * 2)

            if n_column < 0:
                n_column = -((-n_column) % ((c - 1) * 2))
            else:
                n_column = n_column % ((c - 1) * 2)

            while not (0 <= n_row < r and 0 <= n_column < c):
                if n_row < 0:
                    direction += 1
                    n_row = n_row * -1
                elif n_row >= r:
                    direction -= 1
                    n_row = (r - 1) - (n_row - (r - 1))
                elif n_column < 0:
                    direction -= 1
                    n_column = n_column * -1
                elif n_column >= c:
                    direction += 1
                    n_column = (c - 1) - (n_column - (c - 1))

            shark.row = n_row
            shark.column = n_column
            shark.direction = direction

            if n_board[shark.row][shark.column] is None:
                n_board[shark.row][shark.column] = shark
            else:
                # 최종 이동지점에 다른 상어가 있을 때크기 작은걸 제거
                other = n_board[shark.row][shark.column]
                if shark.size > other.size: # 새로 유입되는 상어가 더 크면
                    remove_sharks.append(other)
                    n_board[shark.row][shark.column] = shark
                else:
                    remove_sharks.append(shark)

        for r_shark in remove_sharks:
            sharks.remove(r_shark)
        board = n_board

    return ret;

print(solution())