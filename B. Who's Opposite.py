# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())
for i in range(n):
    a, b, c = list(map(int, input().split()))
    x = abs(a - b)
    if c > 2 * x or a > 2 * x or b > 2 * x:
        print(-1)
    else:
        if c > x:
            t = c - x
        else:
            t = c + x
        print(t)
