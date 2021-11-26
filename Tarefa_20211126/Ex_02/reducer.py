#!/usr/bin/env python3

import sys
from itertools import groupby
from operator import itemgetter

SEP = '\t'


class Reducer(object):

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write(f"{key}{self.sep}{value}\n")

    def reduce(self):
        for current, group in groupby(self, itemgetter(0)):
            try:
                lines_arr = []

                for item in group:
                    lines_arr.append(item[1])
                self.emit(current, lines_arr)
            except ValueError:
                pass

    def __iter__(self):
        for line in self.infile:
            yield line.rstrip().split(self.sep, 1)


if __name__ == "__main__":
    reducer = Reducer()
    reducer.reduce()
