n = int(input())
if n <= 2500: 
    a, b = divmod(n, 25)
    if b == 0:
        print(1, a, 25)
    else:
        print(1, a + 1, b)
elif n <= 7500:
    a, b = divmod(n - 2500, 50)
    if b == 0:
        print(2, a, 50)
    else:
        print(2, a + 1, b)
else:
    a, b = divmod(n - 7500, 25)
    if b == 0:
        print(3, a, 25)
    else:
        print(3, a + 1, b)
