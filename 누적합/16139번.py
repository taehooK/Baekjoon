import sys

input = sys.stdin.readline
string = input().strip()
q = int(input())

prefix_sum = [[0 for i in range(26)]]
for i in range(len(string)):
    temp = prefix_sum[-1][:]
    temp[ord(string[i]) - 97] += 1
    prefix_sum.append(temp)

for _ in range(q):
    a, l, r = input().split()

    print(prefix_sum[int(r) + 1][ord(a) - 97] - prefix_sum[int(l)][ord(a) - 97])
