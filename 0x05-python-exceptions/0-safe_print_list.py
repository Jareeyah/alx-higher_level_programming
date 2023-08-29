#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if (my_list is None or x < 0):
        return (0)
    s = 0
    try:
        while (s < x):
            print("{}".format(my_list[s]), end="")
            s = s + 1
    except IndexError:
        print("")
        return (s)
    print("")
    return (s)
