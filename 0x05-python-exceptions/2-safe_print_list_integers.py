#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if (my_list is None or x < 0):
        return 0

    s = 0
    for p in range(0, x):
        try:
            print("{:d}".format(my_list[p]), end="")
            s = s + 1
        except (ValueError, TypeError):
            continue
        print()
        return s
