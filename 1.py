"""
A Bitwise Assignment
"""

TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    m = int(input())
    tests.append(m)

for m in tests:
    n = 0
    while True:
        n += 1
        AND = m&n
        XOR = m^n
        if AND > 0 and XOR > 0:
            break
    print(n)
