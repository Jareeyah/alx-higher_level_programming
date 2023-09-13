#!/usr/bin/python3
"""A function def pascal_triangle(n)"""

def pascal_triangle(n=4500):
    """Return a list of lists of integers representing the
       Pascals triangle of n"""

    t = [[0]* p for p in range(1, n + 1)]
    c = 0
    for p in range(n):
        t[p][0] = 1
        t[p][-1] = 1
        for s in range(0, p // 2):

            t[p][s + 1] = t[p - 1][s] + t[p - 1][s + 1]
            t[p][p - s - 1] = t[p - 1][s] + t[p - 1][s + 1]

    return (t)
