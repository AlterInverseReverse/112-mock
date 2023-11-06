from bisect import bisect


n, q = map(int, input().split())
arr = list(range(n))
ans = 0
for _ in range(q):
    l, r = map(int, input().split())
    if l != r:
        l, r = min(l, r) - 1, max(l, r) - 1
        # i - the number of elements going back to be "sorted"
        # j - the number of elements going to be "unsorted"
        i, j = bisect(sorted(arr[l + 1:r + 1]), arr[l]), bisect(sorted(arr[l:r]), arr[r])
        ans += 2 * (j - i) + (1 if i > j else -1)
        arr[l], arr[r] = arr[r], arr[l]

    print(ans)
