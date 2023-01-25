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
    # print()
    # print(n, a, s)
    FLAG = True
    splits = [char for char in s]
    uniq_spilts = set(splits)
    for select_char in uniq_spilts:
        checks = []
        for position, char in enumerate(s):
            if char == select_char:
                # print(position)
                checks.append(a[position])
        if len(set(checks)) != 1:
            FLAG = False
            break
    if FLAG:
        print("YES")
    else:
        print("NO")
