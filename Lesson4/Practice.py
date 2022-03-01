# Print out  with For Loop
# 1st Task
# i = 0
# for i in range (-12,-1):
#     i += 1
#     print(i, end=' ')
#
# # Second Task
# print('\n')
# num = 14
# while num > 1:
#     num -= 1
#     print(num)
#
# # Third task
# num1 = 31
# print('Numbers from 33 to 67: ')
# while num1 < 67:
#     num1 += 2
#     print(num1, end=' ')
#
# print('\n')
# for i in range(33, 67+1, 2):
#     print(i, end=' ')
# там если стоит увеличение счетчика на 1 число break не нужен
number =33
while number < 68:
    number += 1
    if number % 2 ==0:

        print(number, end =' ')

print('\n')
num = 33
while True:
    num += 1
    if num % 2 == 0:
        print(num, end=' ')

    if num == 67:
        break