# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


a = input()
if a == ((a[0]).lower() + (a[1:]).upper()):
    print(a.capitalize())
elif a == a.upper():
    print(a.lower())
else:
    print(a)