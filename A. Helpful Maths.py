

#qq=arr.replace("+", "")
# q1=list(qq.split())
# print(q1.sort())
s = input()
n1 = n2 = n3 = 0
for i in range(0, len(s), 2):
    if s[i] == '1':
        n1 += 1
    elif s[i] == '2':
        n2 += 1
    else:
        n3 += 1
ss = "1+" * n1 + "2+" * n2 + "3+" * n3
print(ss)
print(ss[:-1])

#another way
# arr= input()
# value= []
#
#
# for x in range(0,len(arr)):
#     if arr[x] == '1' or arr[x] == '2' or arr[x] == '3':
#         value.append(arr[x])
# value.sort()
# sum_value = "+".join([c for c in value])
#
# print(sum_value)



# main_value=[]
# for i in range(0,len(value)):
#     if value[i] == '1' or value[i] == '2' or value[i] == '3':
#         main_value.append("+".join(value[i]))
# print(main_value)