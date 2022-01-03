# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


t = int(input())
for _ in range(t):
    p=input()
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    e,f = map(int,input().split())
    s = abs(a-c)+abs(b-d)
    if ((a==c==e) and (b<f<d or b>f>d))or ((b==f==d) and (a<e<c or a>e>c)):
        s=s+2
    print(s)