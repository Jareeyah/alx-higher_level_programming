#!/usr/bin/python3
"""A function that inserts a line of text to a file
   after each line containing a specific string (see example)
"""

def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file"""

    new_line = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            new_line = new_line + [line]
            if line.find(search_string) != -1:
                new_line = new_line + [new_string]

    with open(filename, 'w', encoding="utf-8") as file:
        file.write("".join(new_line))
