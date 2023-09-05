#!/usr/bin/python3

def weight_average(my_list=[]):
    new_list = []
    c = 0
    if (len(my_list) == 0):
        return (0)
    for w in my_list:
        new_list.append(w[0] * w[1])
        c += w[1]
    return (sum(new_list) / c)
