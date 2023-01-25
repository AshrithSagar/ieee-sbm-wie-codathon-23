"""
Loids Watch
"""
import math


LARGE = 1000
TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    line = input()
    s, x = line.split(" ")
    tests.append((s, x))

def is_palindrome(num):
    return reverse(num) == num

def reverse(num):
    return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + reverse(num // 10))


for s, x in tests:
    count = 0
    x = int(x)
    for times in range(LARGE):
        HH, MM = [int(d) for d in s.split(":")]
        MM += x

        if MM > 59:
            HH += 1
            MM %= 60
        if HH > 23:
            HH %= 24

        NUM = "".join([str(HH), str(MM)])
        count += int(is_palindrome(int(NUM)))
    print(count)
