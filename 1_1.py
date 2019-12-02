#!/usr/bin/env python3.7

import sys
import math

def main(filename):
    with open(filename) as filehandle:
        fuel_required = [
            math.floor(int(line) / 3) - 2 for line in filehandle
        ]
    print(sum(fuel_required))

if __name__ == '__main__':
    main(filename=sys.argv[1])