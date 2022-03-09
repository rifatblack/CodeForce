
n = int(input())
ans = ""
c = 'a'
for i in range(1,n+1):
	ans+=c
	if(c=='d'):
		c = 'a'
	else:
		c = chr(ord(c)+1)
print(ans)