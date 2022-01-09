import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

t=int(input())
while t:
    l=list(map(int,input().split()))
    l.sort()
    if (l[0]==l[1] and l[2]%2==0) or (l[1]==l[2] and l[0]%2==0) or l[2]==(l[1]+l[0]):
        print("YES")
    else:
        print("NO")
    t-=1