class Fire:
    def __init__(self, row, column, m, s, d):
        self.row = row
        self.column = column
        self.m = m
        self.s = s
        self.d = d
        self.others = []

    def merge(self, other):
        self.others.append(other)

    def division(self):
        ret = []
        sum_m = self.m
        sum_s = self.s
        d_check = self.d % 2
        length = 1 + len(self.others)

        for fire in self.others:
            sum_m += fire.m
            sum_s += fire.s
            d_check += fire.d % 2

        new_m = sum_m // 5
        new_s = sum_s // length

        if new_m <= 0:
            return
        directions = [1, 3, 5, 7]
        if d_check <= 0 or d_check >= length:
            directions = [0, 2, 4, 6]

        for i in range(4):
            ret.append(Fire(self.row, self.column, new_m, new_s, directions[i]))
        return ret
        # 방향이 모두 홀수이거나 짝수인면 [0, 2, 4, 6] 그게아니면 [1, 3, 5, 7]

dy =[-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def solution():
    n, m, k = map(int, input().split())
    fires = []

    for _ in range(m):
        r, c, mass, s, d = map(int, input().split())
        fires.append(Fire(r - 1, c - 1, mass, s, d))

    for _ in range(k):
        board = [[None for i in range(n)] for _ in range(n)]
        new_fires = []
        merged_fires = set()
        for fire in fires: #1.불의 개수만큼 반복
            s = fire.s % n
            n_row = fire.row + dy[fire.d] * s
            n_column = fire.column + dx[fire.d] * s

            if n_row < 0:
                n_row = n + n_row
            if n_row >= n:
                n_row = n_row - n
            if n_column < 0:
                n_column = n + n_column
            if n_column >= n:
                n_column = n_column - n

            fire.row = n_row
            fire.column = n_column

            if board[n_row][n_column] is None:
                board[n_row][n_column] = fire
                new_fires.append(fire)
            else:
                board[n_row][n_column].merge(fire)
                merged_fires.add(board[n_row][n_column])

        for fire in merged_fires:
            division_fires = fire.division()
            new_fires.remove(fire)
            if division_fires is not None:
                new_fires.extend(division_fires)

        fires = new_fires

    ret = 0
    for fire in fires:
        ret += fire.m

    return ret

print(solution())
         #1.1. 다음 좌표를 구한다.
         #1.2. 다른 불이 이미 있으면
         #1.2.1. 이동한다.
         #1.2.2. 기록한다.
         #1.3. 다른 불이 없으면 이동한다. (새로운 fires에도 저장)
        #2. 합쳐진 불의 개수만큼 반복한다.
        # 2.1. 분할한다.
        # 2.1.1.
        # 2.2. 질량이 0이 아니면
        #  2.2.1. fires에 저장한다.

        #3. 불의 개수만큼 반복
        # 3.1. 질량의 합을 구한다.








