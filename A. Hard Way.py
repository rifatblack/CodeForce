# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w

for _ in range(int(input())):
    l=[]
    for i in range(3):
        a,b=map(int,input().split())
        l.append([a,b])
    l.sort(key= lambda point:point[1])
    ans=0
    if l[-1][1]==l[-2][1]:
        ans+=abs(l[-1][0]-l[-2][0])
    print(ans)