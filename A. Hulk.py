# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
i=1
s="I hate "
while i<n:
	if i%2==1:
		s+="that I love "
	else:
		s+="that I hate "
	i+=1
s+="it"
print(s)