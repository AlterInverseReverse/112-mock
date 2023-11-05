for i in range(1, int(input()) + 1):
    visited = set()
    start = input()
    s = start
    while s != '1':
        if s in visited:
            break
        visited.add(s)
        s = str(sum(k * k for k in map(int, s)))
    else:
        print('Case #%d: %s is a Happy number.' % (i, start))
        continue
    print('Case #%d: %s is an Unhappy number.' % (i, start))
