"""
Loids Watch
"""
import math


LARGE = 60 * 24  # Periodic with 1440 atleast.
TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    line = input()
    s, x = line.split(" ")
    tests.append((s, x))

def is_palindrome(num):
    """ Check for palindrome. Returns bool. """
    return reverse(num) == num

def reverse(num):
    """ Return reverse of a number. Recursive function. """
    return int(num != 0) and ((num % 10) * (10**int(math.log(num, 10))) + reverse(num // 10))

def append_0(num):
    """ Add a 0 to the string if number is single digit. Returns string """
    return ("0" if num < 10 else "") + str(num)

for s, x in tests:
    COUNT = 0
    x = int(x)
    HH, MM = [int(d) for d in s.split(":")]
    HH_0, MM_0 = HH, MM
    for times in range(LARGE):
        HH_s, MM_s = append_0(HH), append_0(MM)
        print(HH_s, MM_s)
        NUM = int("".join([HH_s, MM_s]))
        print(NUM, is_palindrome(NUM))
        COUNT += int(is_palindrome(NUM))

        MM += x
        HH += MM//60
        HH %= 24
        MM %= 60
        if HH == HH_0 and MM == MM_0:
            break
    print(COUNT)
