#!/usr/bin/python3i

def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
    except Exception as error:
        return False
    else:
        return True
