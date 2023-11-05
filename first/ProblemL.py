for line in iter(input, '0'):
    s = line
    while len(s) != 1:
        s = str(sum(map(int, s)))
    print(s)
