import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for i in range(0,n-1):
        m=max(m,a[i]*a[i+1])
    print(m)