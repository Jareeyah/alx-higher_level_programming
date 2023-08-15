#!/usr/bin/python3
def no_c(my_string):
    copy = [m for m in my_string if m != 'c' and m != 'C']
    return ("".join(copy))
