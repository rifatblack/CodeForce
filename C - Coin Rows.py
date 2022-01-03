# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



#Move right - (x,y) to (x, y+1)
#Move left - (x,y) to (x+1, y)
#Alice wants to minimize When
# Alice finishes, Bob starts his journey.
# He also performs the moves to reach (2,m)
# and collects the coins in all cells that he visited,
# but Alice didn't.
#Bob wants to maximize


t=int(input())
while(t):
    t=t-1
    m=int(input())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    y=sum(a1)
    x=0
    ans=10000000000000
    for i in range(m):
        y-=a1[i]
        ans=min(ans,max(x,y))
        x+=a2[i]
    print(ans)














