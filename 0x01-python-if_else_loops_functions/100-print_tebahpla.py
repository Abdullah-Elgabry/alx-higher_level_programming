#!/usr/bin/python3
c = 0
for alph in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alph - c)), end="")
    c = 32 if c == 0 else 0
