

#find largest and smallest number

s= int(input())

maximumNumber= 9
maxValue = s - 9

first_digit = maxValue //10
second_digit = maxValue %10
miniValue = (second_digit*10)+first_digit

print(miniValue,maxValue)

# value=0
# for x in range(0,s+1):
#     value +=x
#
# print(value)