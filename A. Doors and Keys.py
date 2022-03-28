# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


for i in range(int(input())):
	n = list(input())
	sum = 0
	cnt = 0
	dem = 0
	for i in range(len(n)):
		if n[i] == 'R':
			sum-=1
		if n[i] == 'G':
			cnt-=1
		if n[i] == 'B':
			dem-=1
		if sum == -1 or cnt ==-1 or dem ==-1:
			print("NO")
			break
		if n[i] == 'r':
			sum+=1
		if n[i] =='g':
			cnt+=1
		if n[i] == 'b':
			dem+=1
	if sum == 0 and cnt == 0 and dem ==0:
		print("YES")