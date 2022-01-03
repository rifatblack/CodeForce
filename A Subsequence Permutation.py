# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

for _ in range(int(input())):
    n=int(input())
    s=list(input())
    sn=sorted(s)
    ans=0
    for z in range(n):
        if s[z]!=sn[z]:
            ans+=1
    print(ans)