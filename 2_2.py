#!/usr/bin/env python

import sys
import copy

def mult(values):
    v1,v2 = values
    return v1 * v2

def get_op(opcode):
    if opcode == 1:
        return sum
    elif opcode == 2:
        return mult

def intcode(codes):
    index = 4
    opcode = None
    while index < len(codes):
        opcode, source1, source2, target = codes[index-4: index]
        if opcode == 99:
            break
        codes[target] = get_op(opcode)([codes[source1], codes[source2]])
        index += 4
    return codes[0]

def main(filename):
    with open(filename) as filehandle:
        original_codes = [int(l) for l in filehandle.read().split(',')]
    for noun in range(100):
        for verb in range(100):
            codes = copy.deepcopy(original_codes)
            codes[1] = noun
            codes[2] = verb
            output = intcode(codes)
            if output == 19690720:
                print(100 * noun + verb)


if __name__ == '__main__':
    main(sys.argv[1])