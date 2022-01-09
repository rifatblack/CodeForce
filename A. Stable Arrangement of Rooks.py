# import sys
# sys.stdin = open('input2.txt', 'r')
# sys.stdout = open('output.txt', 'w')


for _ in range(int(input())):
    n, k = map(int, input().split())

    if (n + 1) // 2 < k:
        print(-1)

    else:
        desk = [['.' for i in range(n)] for i in range(n)]
        for i in range(0, 2 * k, 2):
            desk[i][i] = 'R'

        for row in desk:
            print(''.join(row))