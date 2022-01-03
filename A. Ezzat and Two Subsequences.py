# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



t=int(input())
for i in range(t):
	n=int(input())
	lst=[int(i) for i in input().split()]
	lst.sort()
	a=lst.pop()
	b=sum(lst)/(n-1)
	print('%.9f'%(a+b))

