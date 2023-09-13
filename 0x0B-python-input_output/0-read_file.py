#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):
    """
    Read the filename

    """

    with open(filename, "r", encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
