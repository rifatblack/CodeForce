# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


y=int(input())+1
while len(set(str(y)))<4:
    y+=1
print (y)