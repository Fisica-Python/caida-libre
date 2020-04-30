import math


def pos_vertical(h_0, v_0, t):
    return h_0 + v_0 * t - 4.9 * (t ** 2)


def tiempo_1(v, y):
    return (-v + math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)


def tiempo_2(v, y):
    return (-v - math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)

def tiempo_caida_libre(v_0, h_0):
    # a partir de la ecuación de posición: y = h_0 +v_0t -gt²/2
    # despejamos t igualando y = 0 (pues está en el suelo!)
    # como es una ecuación de segundo grado nos arrojará dos resultados
    # que llamaremos t1 y t2. Descartamos la solución negativa.
    t1 = tiempo_1(v_0, h_0)
    t2 = tiempo_2(v_0, h_0)
    return round(max(t1, t2), 2)