# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

a=input()
x=a.count("4")
y=a.count("7")
z=x+y
print("YES" if(z==4 or z==7) else "NO")