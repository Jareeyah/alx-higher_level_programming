#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_list = []
    for c, d in a_dictionary.items():
        if (d == value):
            new_list.append(c)

        for m in new_list:
            del a_dictionary[m]
        return (a_dictionary)
