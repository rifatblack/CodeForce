# import sys
#
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


for i in range(int(input())):
    n = int(input())
    s = input()
    a = ""
    for i in s:
        if i == "U":
            a+="D"
        elif i == "D":
            a+="U"
        else:
            a+=i
    print(a)

# n=int(input())
#
# for _ in range(n):
#     t= input()
#     st= str(input())
#     ans=''
#     ans2 = ''
#     if st == "U":
#         print("D")
#     # elif st == "D":
#     #     print("U")
#     elif st == "LR":
#         print(st)
#
#     # elif st.replace("D", "U"):
#     #     x = st.replace("D", "U")
#     #     ans +=x
#
#     # elif st.replace("U", "D"):
#     #     x = st.replace("D", "U")
#     #     print(x)
#
#     elif re.findall("U", st):
#         x1 = re.findall("U", st)
#         for _ in range(len(x1)):
#             ans2 += "D"
#
#     print(ans)
#     print(ans2)

