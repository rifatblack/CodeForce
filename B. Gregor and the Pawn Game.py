# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s2=input()
    a=list(s1)
    b=list(s2)
    c=1
    for j in range(n):
        if b[j]=="1":
            if a[j]=="0":
                c=c+1
            elif j>0 and a[j-1]=="1":
                c=c+1
                a[j-1]="!"
            elif j<n-1 and a[j+1]=="1":
                c=c+1
                a[j+1]="!"
    print(c)