#!/usr/bin/python3

def safe_function(fct, *args):
     import sys
     try:
         res = fct(*args)
         return (res)
     except sys.exc_info()[0]:
         print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
         return (None)
