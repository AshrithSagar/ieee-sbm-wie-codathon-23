"""
Loids Watch
"""
REPEAT = 60 * 24  # Periodic with 1440 atleast.
TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    line = input()
    s, x = line.split(" ")
    tests.append((s, x))

def is_palindrome(string):
    """ Check for palindrome. Returns bool. """
    return string[::-1] == string

def append_0(num):
    """ Add a 0 to the string if number is single digit. Returns string """
    return ("0" if num < 10 else "") + str(num)

for s, x in tests:
    COUNT = 0
    x = int(x)
    HH, MM = [int(d) for d in s.split(":")]
    HH_0, MM_0 = HH, MM
    for times in range(REPEAT):
        HH_s, MM_s = append_0(HH), append_0(MM)
        NUM = "".join([HH_s, MM_s])
        COUNT += int(is_palindrome(NUM))

        MM += x
        HH += MM//60
        HH %= 24
        MM %= 60
        if HH == HH_0 and MM == MM_0:
            break
    print(COUNT)
