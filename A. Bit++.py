

n = int(input())

value = 0

for i in range(n):
    each_statement = input()
    if each_statement[0] == '+' or each_statement[1] == '+':
        value +=1

    else:
        value -=1

print(value)