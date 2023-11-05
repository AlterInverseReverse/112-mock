n = int(input())

for _ in range(n):
    k = int(input())
    xs = list(map(int, input().split()))
    t = 0
    for i in range(k):
        for j in range(1, k - i):
            if xs[j - 1] > xs[j]:
                xs[j - 1], xs[j] = xs[j], xs[j - 1]
                t += 1
    print('Optimal train swapping takes %d swaps.' % t)
