group = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input())
for _ in range(n):
    i = 0
    m, d = map(int, input().split())
    m, d = m - 1, d - 1
    for j in range(m):
        i += days[j]
    i += d
    print(group[i % 7])

