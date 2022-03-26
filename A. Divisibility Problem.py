# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())
capacity = 0
for p in range(n):
    x, y = [int(i) for i in input().split()]
    if x % y == 0:
        print(0)
    else:
        print(y - x % y)