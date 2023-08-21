#!/usr/bin/python3

if (__name__ == "__main__"):
    import sys
    from calculator_1 import add, mul, sub, div

    if (len(sys.argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operators = ["*", "+", "-", "/"]
    args = sys.argv
    x = args[1]
    y = args[2]
    z = args[3]
    if y not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if args[2] == '+':
            print("{} {} {} = {}".format(x, y, z, add(int(x), int(z))))
        elif args[2] == "*":
            print("{} {} {} = {}".format(x, y, z, mul(int(x), int(z))))
        elif args[2] == '/':
            print("{} {} {} = {}".format(x, y, z, div(int(x), int(z))))
        elif args[2] == '-':
            print("{} {} {} = {}".format(x, y, z, sub(int(x), int(z))))
