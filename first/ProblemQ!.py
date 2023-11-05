from bisect import bisect


n, q = map(int, input().split())
xs = list(range(n - 1, -1, -1)) 

for _ in range(q):
    l, r = map(int, input().split())
    xs[l - 1], xs[r - 1] = xs[r - 1], xs[l - 1]

    ys = []
    ans = 0
    for i, x in enumerate(reversed(xs)):
        j = bisect(ys, x)
        ans += i - j
        ys.insert(j, x)
    print(ans)
