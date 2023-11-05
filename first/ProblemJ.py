import sys


lines = sys.stdin.readlines()
for line in lines:
    n = int(line.strip())
    k = 1
    for i in range(1, n):
        k += i
    print(k)
