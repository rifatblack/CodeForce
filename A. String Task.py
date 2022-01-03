

# string = str(input())
#
# arr=[]
# for x in range(len(string)):
#     if string[x] == 'a' or string[x] == 'A' or string[x] == 'e' or string[x] == 'E' or string[x] == 'i' or string[x] == 'I' or string[x] == 'o' or string[x] == 'O' or string[x] == 'u' or string[x] == 'U' or string[x] == 'y' or string[x] == 'Y':
#         print(string[x])
#         arr.append('.')
#         arr.append(string[x+1])
#     else:
#
#
# print(arr)

# string = input("Enter any string: ")
# if string == 'x':
#     exit()
# else:
#     newstr = string
#     print("\nRemoving vowels from the given string")
#     vowels = ('a', 'e', 'i', 'o','y','u','A','E','I','O','U','Y')
#     for x in string:
#         if x in vowels:
#             newstr = newstr.replace(x,"")
#     print("New string after successfully removed all the vowels:")
#     print(newstr.lower())
#
#     value=[]
#     for x in range(len(newstr)):
#         if 1 % x !=0:
#             value.append('.')

string =input().lower()
notvowl = ".".join([c for c in string if not c in "aiueoy"])

print ("." + notvowl)

