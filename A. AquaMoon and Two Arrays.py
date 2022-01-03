# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
    s = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    inc=[]
    dec=[]
    for i in range(s):
        if(a[i]!=b[i]):
            if(a[i]<b[i]):
                inc+=[i+1]*(b[i]-a[i])
            else:
                dec+=[i+1]*(a[i]-b[i])
    if(len(inc)!=len(dec)):
        print(-1)
    else:
        print(len(inc))
        for i in range(len(inc)):
            print(dec[i],inc[i])