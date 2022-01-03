
#N stones on table in row
# each them can be red , green, blue

# n=int(input())
# string = str(input())
#
# n1=0
#
# for x in range(len(string)-1):
#     if string[x] == string[x+1]:
#         n1 +=1
#     else:
#         continue
#
# print(n1)



string = str(input())

n1=0

for x in range(0,len(string)-1):
    print(x)
    if string[x-1] == string[x+1]:
        n1 +=1
    else:
        continue

print(n1)

