# number = 5.5
#
# if number > 0.0:
#    pass # pass is null statement, can be used for create loops
#
# '''pass is just a placeholder for
# functionality to be added later.'''
# # sequence = {'p', 'a', 's', 's'}
# # for val in sequence:
# #     pass


# define a function before using
# def greet(name):
#      print('Hello', name)
#      return # control the program
#      print('How do you do')
#
# # Python arguments
# greet('Jack') # Jack is argument

# def add_number(n1, n2):
#     result = n1+n2
#     # print('The sum is', result)
#     return result
#
# number1 = 5.4
# number2 = 6.7
# result = add_number(number1, number2)
# print('The sum is: ', result)

# function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

# calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks <= 50:
        grade = 'C'
    else:
        grade = 'C'
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print('Your average marks is: ', average_marks)

grade = compute_grade(average_marks)
print('Your grade is', grade)
# length = len(marks)
# print('Length is: ', length)
#
# marks_sum = sum(marks)
# print('The total marks you got is: ', marks_sum)

# function to add numbers
def add_numbers(n1, n2):
    return n1 + n2

# function to multiply result
def multiply_numbers(n1, n2):
    return n1 * n2

n1= 65
n2 = 48

sum_result = add_numbers(n1,n2)
print('The result of adding: ', sum_result)

product_result = multiply_numbers(n1, n2)
print('The product of multiplication is: ', product_result)
