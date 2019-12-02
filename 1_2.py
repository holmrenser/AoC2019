#!/usr/bin/env python3.7

import sys
import math

def recursive_fuel_calc(mass):
    fuel_required = math.floor(mass / 3) - 2
    if fuel_required <= 0:
        return 0
    yield fuel_required
    yield from recursive_fuel_calc(fuel_required)

def main(filename):
    with open(filename) as filehandle:
        fuel_required = [
            sum(recursive_fuel_calc(int(line))) for line in filehandle
        ]
    print(sum(fuel_required))

if __name__ == '__main__':
    main(filename=sys.argv[1])