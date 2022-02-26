num = int(input('Enter a number please: '))
#  Task1
if num < 9 and num > 2:
    print('Number greater than 2 and less than 9')
else:
    print('Unknown number')
#  Task 1 with ternary operator
print('Number greater than 2 and less than 9' if num < 9 and num > 2 else 'Unknown number')

# task2
packageWeight = float(input('Please enter a weight of package: '))
if packageWeight >= 0 and packageWeight <= 2:
    print('Your package calculate is at rate of 3.5$ per kg')
elif packageWeight >= 3 and packageWeight <= 5:
    print('Your package calculate is at rate of 5.5$ per kg')
elif packageWeight >=6 and packageWeight <=10:
    print('Your package calculate is at rate of 7$ per kg')
elif packageWeight >= 11 and packageWeight <= 50:
    print('Your package calculate is at rate of 10$ per kg')
else:
    print('Package could not be sent')

# Task 3
# Check if number is even or odd
number = int(input('Enter your number: '))
if (number % 2 != 0):
    print('This number is odd(nechetnoe)')
else:
    print('Please restart the program')