#!/usr/bin/python3
def remove_char_at(str, r):
    if (r < 0):
        return(str)
    return(str[:r] + str[r + 1:])
