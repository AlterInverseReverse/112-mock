from collections import Counter


input()
counter = Counter(map(int, input().split()))
ats = counter.most_common()
most = ats[0][1]
print(*sorted(a for a, t in ats if t == most))
