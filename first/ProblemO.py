import math
import sys


lines = sys.stdin.readlines()
for line in lines:
    # 1/2 n^2 + 1/2 n - 1/2 s^2 + 1/2 s >= d
    # 1/2 n^2 + 1/2 n - 1/2 s^2 + 1/2 s - d >= 0
    # -1/2 + sqrt(1/4 + s^2 - s + 2d)
    s, d = map(int, line.strip().split())
    print(int(math.ceil(-0.5 + math.sqrt(0.25 + s**2 - s + 2*d))))
