# 민호와 강호 - 삼분탐색 (어려움..)

import math
import sys

def calc_dist(left):
    mx = Ax * left + Bx * (1-left)
    my = Ay * left + By * (1-left)
    kx = Cx * left + Dx * (1-left)
    ky = Cy * left + Dy * (1-left)
    return math.dist([mx, my], [kx, ky])

def trinary_search(start, end):
    while abs(end - start) > 1e-9:
        left = (2*start + end)/3
        right = (start + 2*end)/3
        if calc_dist(left) > calc_dist(right):
            start = left
        else:
            end = right

    return calc_dist(start)

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())

print("%.10f" % trinary_search(0, 1))