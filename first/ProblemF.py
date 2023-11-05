from functools import reduce
from operator import mul

import sys


i, lines = 0, sys.stdin.readlines()
while i < len(lines):
    w, n = int(lines[i].strip()), int(lines[i + 1].strip())
    i += 2
    area = 0
    for j in range(i, i + n):
        area += reduce(mul, map(int, lines[j].strip().split()))
    i += n
    print(area // w)
