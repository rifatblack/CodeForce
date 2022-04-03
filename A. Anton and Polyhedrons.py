# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

num = int(input())
faces = 0

default_polys = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
default_faces = [4, 6, 8, 12, 20]

for i in range(0, num):
    poly = input()
    if poly in default_polys:
        faces += default_faces[default_polys.index(poly)]

print(faces)