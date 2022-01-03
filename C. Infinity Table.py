from math import sqrt
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t = int(input())
for _ in range(t):
    k = int(input())
    s = int(sqrt(k))
    r = s * s
    e = k - r
    if e == 0:
        print(s, 1)
    elif e <= s:
        print(e, s + 1)
    else:
        print(s + 1, 2 * s + 2 - e)