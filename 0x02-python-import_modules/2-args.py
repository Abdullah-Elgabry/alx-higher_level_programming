#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    pls = len(sys.argv) - 1
    if pls == 0:
        print("0 arguments.")
    elif pls == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(pls))
    for i in range(pls):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
