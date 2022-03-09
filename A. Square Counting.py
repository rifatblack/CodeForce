# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    print(s//(n**2))