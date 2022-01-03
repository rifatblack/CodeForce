import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    i = 1
    b = sorted(a)
    while a!=b:
        if i%2!=0:
            for j in range(0,n-2,2):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
                    print(a[j],a[j+1],'n')
        else:
            for j in range(1,n-1,2):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
                    print(a[j], a[j + 1],'m')
        i = i+1
    print(i-1)
    t = t-1


