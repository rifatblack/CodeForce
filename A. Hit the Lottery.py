# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


balance = int(input())

count=0
count+=balance//100
count+=(balance%100)//20
count+=(balance%20)//10
count+=(balance%10)//5
count+=balance%5
print(count)
