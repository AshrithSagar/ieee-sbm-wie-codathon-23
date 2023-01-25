"""
Ron's IQ
"""
TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    n = input()
    a = input()
    a = a.split(" ")
    s = input()
    tests.append((n, a, s))

for n, a, s in tests:
    print()
    print(n, a, s)
    splits = [char for char in s]
    uniq_spilts = set(splits)
    checks = []
    for select_char in uniq_spilts:
        for position, char in enumerate(s):
            if char == select_char:
                checks.append(a[position])
    print(checks)
