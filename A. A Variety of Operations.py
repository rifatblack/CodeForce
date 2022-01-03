# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


n = int(input())

for x in range(n):
    a,b=map(int,input().split())

    ans= abs(a-b)
    if a==b:
        if a==0 and b==0:
            print(0)
        else:
            print(1)
    elif (a+b)%2!=0:
        print(-1)
    else:
        print(2)