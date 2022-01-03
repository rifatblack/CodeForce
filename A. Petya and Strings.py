
# # Default lexical sorting function
# def LexicalSorting(Orig_str):
#     # using split() function
#     WordOfString = Orig_str.split()
#     # using sort() function
#     WordOfString.sort()
#     # printing string in sorted words
#     for a in WordOfString:
#         print(a)
#
#
# if __name__ == '__main__':
#     # define a string
#     Orig_str = "This is an example string to be sorted in the program"
#     # Printing original string
#     print("Original string: ", Orig_str)
#     # Calling out sorting function
#     print("Sorted string words: ")
#     LexicalSorting(Orig_str)
#
# number = ['aaaa','aaaA']
#
# number.sort()
#
# print(number)



# string1 = input()
# string2 = input()
#
# s1 = string1.lower()
# s2 = string2.lower()
#
# list1=[s1,s2]
#
# list1.sort()
#
# print(list1)
#
#
#
# if list[0] < list[1]:
#     print("-1")
#
# if list[1] < list[0]:
#     print("1")
#
# if list[0] == list[1]:
#     print("0")


# s1 = input()
# s2 = input()
#
# s1 = s1.lower()
# s2 = s2.lower()
#
# s1 = list(s1)
# s2 = list(s2)
#
# var = False
#
# for i in range(len(s1)) :
#     if s1[i] < s2[i] :
#         print(-1)
#         var = True
#         break
#     elif s1[i] > s2[i] :
#         print(1)
#         var = True
#         break
#
# if not var :
#     print(0)




s1 = input()
s2 = input()

s1 = s1.lower()
s2 = s2.lower()

s1 = list(s1)
s2 = list(s2)

var = False

for i in range(len(s1)) :
    if s1[i] < s2[i] :
        print(-1)
        var = True
        break
    elif s1[i] > s2[i] :
        print(1)
        var = True
        break



if var == False :
    print(0)
