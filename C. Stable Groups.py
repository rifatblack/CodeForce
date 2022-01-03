import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
v = []
for i in range(1,n):
    if a[i] - a[i-1]>x:
        v.append((a[i]-a[i-1] - 1)//x)
v.sort(reverse = True)
while(len(v)):
    if v[-1] <= k:
        k-=v[-1]
        v.pop()
    else:
        break
print(len(v)+1)