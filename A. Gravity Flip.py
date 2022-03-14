# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

x = int(input())
n = list(map(int, input().split()))
n.sort()
for i in n:
    print(i, end=" ")