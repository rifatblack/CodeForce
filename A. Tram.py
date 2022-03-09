# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

x=input();t=y=0
for x in range(int(x)):
	d,u=map(int,input().split())
	t+=(u-d)
	y=max(t,y)
print(y)