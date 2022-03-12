# # name = 'Felix'
# # print(name)
# #
# # # name = input('Enter your name: ')
# # # print(name)
# # #
# # number = input('Enter a number: ')
# # # number  = int(number) # convert to integer
# # number = float(number) # convert to float
# # print(type(number))
# #
# # number1 = 5
# # print(type(number1))
# #
# # number2 = 45.5
# # print(type(number2))
#
# # If else Statement
# # if test condition
# # statement(s)
#
# # score = int(input('Enter your score: '))
# score = 105
# # if score >= 50:
# #     print('You have passed your exams')
# #     print('Congratulations')
# #
# # #if score < 50:
# # else:
# #     print('Sorry, you have failed your exam')
#
# if score > 100 or score < 0:
#     print('Score is invalid')
# elif score >= 50:
#     print('You have passed your exams')
#     print('Congratulations')
# else:
#     print('Sorry, you have failed your exam')
#
# number = float(input('Please enter the float number: '))
#
# if number > 0:
#     print('The number is positive')
# elif number < 0:
#     print('The number is negative')
# else:
#     print('The number is 0')
#
# # Solution 3: Using Nested if else
#
# number = float(input("Enter a number: "))
#
# if number >= 0:
#     # At this point, number is either 0 or a positive number
#     if number > 0:
#         print("The number is positive")
#     else:
#         print("The number is 0")
# else:
#     print("The number is negative")
#
#

# Python while loop
# while test condition:
# statement

count = 5

while count < 10:
    print(count)
    count +=1

number = int(input('Enter the number: '))
count = 10
while count >= 1:
    product = number * count
    print(number, 'x', count, '=', product)
    count -= 1






