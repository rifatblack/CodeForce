# n = int(input())
# count = 0
# for i in range(0, n):
#     x = input()
#     if x.count('1') >= 2:
#         count += 1
# print(count)


# input_arr = input().split()
#
# count =0
#
# for i in range(0, len(input_arr)):
#     if int(input_arr[i]) >= 5:
#         count += 1
#list(map(int, input().split()))
# print(count)


# if __name__ == '__main__':
#     # lis = list(map(int, input().split()))[:i]
#
#
#     i = int(input())
#     lis = list(map(int, input().strip().split()))[:i]
#     z = max(lis)
#     while max(lis) == z:
#         lis.remove(max(lis))
#
#     print(max(lis))

# N = int(input())
#
# # Get the input
# numArray = list(map(int, input().split()))
#
# sum_integer = 0
# # Write the logic to add these numbers here
#
#
# for x in range(len(numArray)):
#     if N > 1 and N < 100:
#         sum_integer += numArray[x]
#
#
# # Print the sum
# print(sum_integer)
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

# t = int(input())
# for _ in range(t):
#     n, k = [int(i) for i in input().split()]
#     arr = [int(i) for i in input().split()]
#     sorted_a = sorted(arr)
#     d = dict()
#     for i in range(n):
#         d[sorted_a[i]] = i
#     count = 1
#     for i in range(1, n):
#         # new_idx = sorted_a.index(arr[i - 1]) + 1
#         if d[arr[i - 1]] + 1 == n or arr[i] != sorted_a[d[arr[i - 1]] + 1]:
#             count += 1
#     if count <= k:
#         print('yEs')
#     else:
#         print('nO')

x=8
for i in range(x,7+x):
    print(i)