# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


for i in range (int(input ())):
    num=int(input())
    if num==1:
        print(num)
    elif num==2:
        print(num)
    elif num%3==0:
        print('21'*(num//3))
    elif num%3==1:
        print('12'*(num//3)+'1')
    elif num%3==2:
        print('21'*(num//3)+'2')