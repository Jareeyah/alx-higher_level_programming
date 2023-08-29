#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for m in range(1, 3):
        try:
            if (m > a):
                raise Exception("Too far")
            else:
                res = (res + ((a ** b) / m))
        except Exception:
            res = (a + b)
            break
        return (res)
