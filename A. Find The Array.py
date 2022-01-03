# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


t = int(input())
while t > 0:
    s = int(input()) - 1
    print(int(s ** 0.5) + 1)
    t -= 1