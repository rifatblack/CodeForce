import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

#
# string = str(input())
# x1=len(string)
#
# arr=[]
#
# for x in range(len(string)):
#     arr.append(string[x])
#
# x1=len(arr)-1
#
# yes=False
# yes1 = 0
#
#
# for x in range(x1):
#     if arr[0] == arr[x1]:
#         yes +=True
#         break
#     if arr[x] == "1":
#         yes1 += 1
#
#     # if arr[x] == 1:
#     #     for i in range(x,7+x):
#     #         if 1 == arr[i]:
#     #             yes1 +=1
#
#
#
# if yes:
#     print("YES")
# elif yes1 >= 7:
#     print("YES")
# else:
#     print("No")


s=input()
flag=0
if '1111111' in s:
    flag=-1
if '0000000' in s:
    flag=-1
if(flag==-1):
    print("YES")
else:
    print("NO")
