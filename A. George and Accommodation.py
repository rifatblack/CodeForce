# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input())
zero = 0
lisp, lisq = [], []
for i in range(n):
	p, q = map(int, input().split())
	lisp.append(p) ; lisq.append(q)
	if lisp[i] != lisq[i] and lisq[i] - lisp[i] >= 2:
		zero += 1
print(zero)