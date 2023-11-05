for line in iter(input, '0 0 0 0'):
    h1, m1, h2, m2 = map(int, line.split())
    
    group_h = list(range(24))
    i, hours = h1, 0
    if h1 == h2 and m1 > m2:
        hours += 1
        i += 1
    while group_h[i % 24] != h2:
        hours += 1
        i += 1

    print(hours * 60 + m2 - m1) 
