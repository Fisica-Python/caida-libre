import math
def pos_vertical(h_0, v_0, t):
    return h_0 + v_0 * t - 4.9 * (t ** 2)


def tiempo_1(v, y):
    return (-v + math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)


def tiempo_2(v, y):
    return (-v - math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)