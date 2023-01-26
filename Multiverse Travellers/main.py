"""
Multiverse Travellers
"""
from itertools import product


m = int(input())

demon = input()
ex, fy = [int(x) for x in demon.split(" ")]

travellers = input()
cx, dy = [int(x) for x in travellers.split(" ")]

portal = input()
ax, by = [int(x) for x in portal.split(" ")]

def in_bound(dim, delta):
    """ Check whether dimension will be within the board. Returns bool """
    return (dim+delta >= 1) and (dim+delta <= m)

def calculate_radar(pos_x, pos_y):
    """ Get all possible locations allowed. """
    radar = []
    for delta in range(1, m+1):
        radar.append((pos_x, delta))
        radar.append((delta, pos_y))
        for mult in product([+1, -1], [+1, -1]):
            if in_bound(pos_x, mult[0]*delta) and in_bound(pos_y, mult[1]*delta):
                radar.append((pos_x+mult[0]*delta, pos_y+mult[1]*delta))
    radar = set(radar)
    return radar

demons_radar = calculate_radar(ex, fy)
travellers_radar = calculate_radar(cx, dy)

REACHED = False
blocks = []
paths_to_portal = product(range(min(cx, ax), max(cx, ax)+1), range(min(dy, by), max(dy, by)+1))
for path in paths_to_portal:
    if path in demons_radar:
        blocks.append(path)
print(blocks)
