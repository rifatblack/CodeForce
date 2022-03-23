# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


number = int(input())

if (number % 4 == 0 or number % 7 == 0 or number % 47 == 0 or number % 477 == 0):
    print("YES")
else:
    print("NO")