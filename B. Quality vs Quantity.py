
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

tc = int(input())
for i in range(tc):

    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    x, y = a[0], 0

    for i in range(1, n // 2 + n % 2):
        x += a[i]
        y += a[-i]
        if x < y:
            print('YES')
            break
    else:
        print('NO')