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
    return (dim+delta >= 1) and (dim+delta <= m)

def calculate_radar(x, y):
    radar = []
    for delta in range(1, m+1):
        radar.append((x, delta))
        radar.append((delta, y))
        if in_bound(x, delta) and in_bound(y, delta):
            radar.append((x+delta, y+delta))
        if in_bound(x, -1*delta) and in_bound(y, delta):
            radar.append((x-delta, y+delta))
        if in_bound(x, delta) and in_bound(y, -1*delta):
            radar.append((x+delta, y-delta))
        if in_bound(x, -1*delta) and in_bound(y, -1*delta):
            radar.append((x-delta, y-delta))
    radar = set(radar)
    return radar

demons_radar = calculate_radar(ex, fy)
travellers_radar = calculate_radar(cx, dy)

reached = False
blocks = []
paths_to_portal = product(range(min(cx, ax), max(cx, ax)+1), range(min(dy, by), max(dy, by)+1))
for path in paths_to_portal:
    if path in demons_radar:
        blocks.append(path)
print(blocks)
