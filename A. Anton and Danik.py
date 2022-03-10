# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n = int(input(""))
x = input("")
A = x.count("A")
D = x.count("D")

if D < A:
    print("Anton")
elif D == A:
    print("Friendship")
else:
    print("Danik")