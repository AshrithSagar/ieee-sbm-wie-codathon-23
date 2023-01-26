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

def check_reachable(reached, pos_cx, pos_dy):
    """ Recursive function to get paths. """
    paths_to_portal = product(
        range(min(pos_cx, ax), max(pos_cx, ax)+1),
        range(min(pos_dy, by), max(pos_dy, by)+1))
    for path in paths_to_portal:
        if not reached and path != (pos_cx, pos_dy):
            if path not in demons_radar:
                check_reachable(reached, path[0], path[1])
            if (cx, dy) == (ax, by):
                reached = True
    return reached

REACHED = check_reachable(False, cx, dy)
print("YES" if REACHED else "NO")
