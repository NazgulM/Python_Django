num1 = 10
num2 = 20
num3 = 5
num4 = 10
# compare of numbers

print(num1 > num2)  # False
print(num1 < num2)  # True

print(num1 == num2)  # False
print(num1 != num2)  # True

print(num1 >= num2)  # False
print(num1 <= num2)  # True
print(num1 >= num4)  # True
print(num1 <= num4)  # True

num1 = 10
num2 = 20
num3 = 5
num4 = 10
# compare 3 or more numbers
print(num1 > num2 < num3)  # False
print(num1 > num2 > num3)  # False
print(num1 < num2 > num3)  # True

# compare numbers with "OR" and "AND"
# compare numbers with "!="
optionFalse = False
optionTrue = True
print(optionFalse and optionTrue)  # False
print(optionFalse or optionTrue)  # True
print(optionFalse != optionTrue)  # True
print(optionFalse != optionFalse)  # False

print(num1 != num2)  # True
print(num1 != num4)  # False

letter1 = 'a'
letter2 = 'b'  # as letter after then that has big value
letter3 = 'A'
letter4 = 'B'
print(letter1 > letter2)  # False
print(letter1 < letter2)  # True

print(letter1 > letter3)  # uppercase letter more valuable
print(letter1 < letter3)  # True

weatherCondition = 'There is a rain'
weatherCondition2 = 'There is no rain'

actualWeather = 'There is a rain'

if actualWeather == weatherCondition:
    print('I go outside with umbrella')
else:
    print('I go outside without umbrella')
