


# def ContestResult(each_person):
#
#     count = 1
#     flag2 = 0
#
#     for x in each_person:
#
#         if x in count:
#             print("x")
#         if x == 0:
#             flag2 += 1
#
#
#
#
#
#
# if __name__ == '__main__':
#
#
#     n = int(input("Enter the N element:"))
#
#
#     for i in range(n):
#         each_person = inputs = list(map(str,input("Enter Each person Value:").split()))
#         ContestResult(each_person)


n = int(input())
count1 = 0
for i in range(0, n):
    x = input()
    if x.count('1') >= 2:
        count1 += 1
print(count1)