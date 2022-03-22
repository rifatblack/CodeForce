# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def ans(k,l,m,n,d):
    c = 0
    for i in range(1,d+1):
        if(i%k==0 or i%l==0 or i%m==0 or i%n==0):
            c+=1
    return c
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
print(ans(k,l,m,n,d))