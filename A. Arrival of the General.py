# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())

maior = 0
menor = 2000000000
ma = 0
me = 0

h = list(map(int, input().split()))

for i in range(0, n, 1):
    if (h[i] <= menor):
        menor = h[i]
        me = i
    if (h[i] > maior):
        maior = h[i]
        ma = i

if (ma < me):
    print(ma + abs(n - (me + 1)))
else:
    print(ma + abs(n - (me + 1)) - 1)