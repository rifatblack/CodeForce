# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

k,n,w=map(int,input().split())
r=(((w*(w+1))//2)*k)-n
if r<=0:
    r=0
print(r)

# cost=0
# k,n,w=map(int,input().split())
#
# for x in range(1,w):
#     rate = x * k
#     cost=cost+rate
# loan=cost-n
# if(loan<0):
#     loan=0
# print(loan)

