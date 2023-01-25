"""
Number of groups
"""

TEST_CASES = int(input())

tests = []
for test in range(TEST_CASES):
    line = input()
    a, b, c = [int(x) for x in line.split(" ")]


def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def groupings(a, b, c):
    """
    (a * lcm (x,y)) - (b * hcf(x,y)) = c
    """
    


for m in tests:
    print(m)
