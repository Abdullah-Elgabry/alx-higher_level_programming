#!/usr/bin/python3
for dig_one in range(10):
    for dig_two in range(dig_one, 10):
        if dig_one < dig_two:
            print("{:d}{:d}".format(dig_one, dig_two),
                  end="\n" if dig_one == 8 and dig_two == 9 else ", ")
