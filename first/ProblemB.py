mapping = {
        'Tetrahedron': 4,
        'Cube': 6,
        'Octahedron': 8,
        'Dodecahedron': 12,
        'Icosahedron': 20,
}

s = 0
for _ in range(int(input())):
    s += mapping[input()]
print(s)
