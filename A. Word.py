# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s = str(input())
if sum(map(str.islower, s)) >= len(s)/2:
    print(s.lower())
else:
    print(s.upper())