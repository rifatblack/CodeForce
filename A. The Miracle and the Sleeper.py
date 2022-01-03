import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


n = int(input())

for x in range(n):
    a,b=map(int,input().split())

    if a==b:
        print("0")
    else:
        if a>(b/2):
            print(b%(a))
        if a<=b/2:
            r=int(b/2)
            k=int(b%r)
            t=int(b%(r+1))
            print(max(k,t))














