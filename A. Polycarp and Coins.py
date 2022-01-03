# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

# for i in range(int(input())):
# 	n=int(input())
# 	if n%3==0:
# 		print(n//3,n//3)
# 	elif n%3==1:
# 		print(n//3+1,n//3)
# 	else:
# 		print(n//3,n//3+1)
n=int(input())

for i in range(n):
    m=int(input())
    div= m / 3
    remi= m % 3
    if remi==1:
        print(int(div+remi),int(div))
    elif remi==2:
        print(int(div),int(div+1))
    else:
        print(int(div), int(div))


