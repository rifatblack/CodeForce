# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())
for i in range(n):
    input()
    xs = [int(i) for i in input().split()]
    ys = [0, 0]
    for x in xs:
        ys[x % 2] += 1

    if ys[0] == ys[1]:
        print("Yes")
    else:
        print("No")