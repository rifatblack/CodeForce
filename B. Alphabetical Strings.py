# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


for _ in range(int(input())):
   s=input()
   ans="YES"
   n=len(s)
   i=0
   j=n-1
   char=97+(n-1)
   while n>0:
       if s[i]==chr(char):
           i+=1
       elif s[j]==chr(char):
           j-=1
       else:
           ans="NO"
           break
       char-=1
       n-=1
   print(ans)