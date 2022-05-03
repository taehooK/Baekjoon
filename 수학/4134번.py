import math
import sys

input = sys.stdin.readline
def solution():
    t = int(input())
    for _ in range(t):
        number = int(input())
        print(next_prime(number))

def next_prime(number):
    number_temp = number
    while not is_prime(number_temp):
        number_temp += 1
    return number_temp
def is_prime(number):
    if number <= 1:
        return False
    max = int(math.sqrt(number))

    temp = 2
    while temp <= max:
        if number % temp == 0:
            return False
        temp += 1
    return True

solution()
