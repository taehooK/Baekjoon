import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n + 1)
tree = [0] * (n + 1)

# i번째 수까지의 누적합을 계산
def prefix_sum(i):
    result = 0
    while i > 0:
        result + tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= ( i & -i)

# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    # 업데이트 연산인 경우
    if a == 1:
        update(b, c - arr[b]) # 바뀐 크기 만큼 적용
        arr[b] = c
        #구간 합 연산 인 경우
    else:
        print(interval_sum(b, c))


