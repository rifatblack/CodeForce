# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


t=int(input())
while t:
    t-=1
    n=int(input())
    arr=list(map(int,input().split()))
    temp=sum(arr)%n
    print(temp*(n-temp))