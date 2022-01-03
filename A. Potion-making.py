# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

from math import gcd
t = int(input())
for _ in range(t):
    k = int(input())
    print(100 // gcd(k, 100))