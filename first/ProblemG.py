for line in iter(input, '0'):
    n = int(line)
    print(n * (n + 1) * (2 * n + 1) // 6)
