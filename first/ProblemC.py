import sys


lines = sys.stdin.readlines()
for line in lines:
    v, t = map(int, line.strip().split())
    print(2 * v * t)
