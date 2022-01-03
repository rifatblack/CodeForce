# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n,q = [int(x) for x in input().split()]
s = input()
g = [0]
val = 0
for i in s:
	val += ord(i)-96
	g.append(val)
for i in range(q):
	d = {}
	l,r = [int(x) for x in input().split()]
	print(g[r]-g[l-1])