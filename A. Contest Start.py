# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



k=int(input())
for i in range(k):
    n,x,t=list(map(int,input().split()))
    m=min(n-1,t//x)
    if m==0:
        print(0)
    else:
        myans=(m*(m-1)//2)+m*(n-m)
        print(myans)

