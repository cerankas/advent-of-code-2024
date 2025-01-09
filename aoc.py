import sys
import re

def input_data():
    script_name = sys.argv[0]
    day = ints(script_name)[-1]
    return open(f'{day}.txt').read()

def ints(txt:str):
    return list(map(int, re.findall(r'(-?\d+)', txt)))

def optimize_for_zero(fun, show = False):
    x1, x2 = -1, 1
    s = 1 if fun(x1) < fun(x2) else -1
    while fun(x1) * s > 0: x1 *= 10
    while fun(x2) * s < 0: x2 *= 10
    while 1:
        x = (x1 + x2) // 2
        f = fun(x) * s
        if show: print(x, f)
        if f > 0:
            x2 = x
            continue
        if f < 0:
            x1 = x
            continue
        return x

