# Keywords are the reserved words in Python.
#
# We cannot use a keyword as a variable name, function name or any other identifier.
# They are used to define the syntax and structure of the Python language.
#
# In Python, keywords are case sensitive.
#
# There are 33 keywords in Python 3.7. This number can vary slightly over the course of time.
#
# All the keywords except True, False and None are in lowercase and they must be written as they are.
# The list of all the keywords is given below.
# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield

#Rules for writing identifiers
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit.
# 1variable is invalid, but variable1 is a valid name.
# Keywords cannot be used as identifiers.
# global = 1

# We cannot use special symbols like !, @, #, $, % etc. in our identifier.

# An identifier can be of any length.
# Things to Remember
# Python is a case-sensitive language. This means, Variable and variable are not the same.
#
# Always give the identifiers a name that makes sense. While c = 10 is a valid name, writing count = 10 would make more sense, and it would be easier to figure out what it represents when you look at your code after a long gap.
#
# Multiple words can be separated using an underscore, like this_is_a_long_variable.

# Multi-line statement
# In Python, the end of a statement is marked by a newline character. But we can
# make a statement extend over multiple lines with the line continuation character (\). For example:
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

#This is an explicit line continuation.
# In Python, line continuation is implied inside parentheses ( ),
# brackets [ ], and braces { }. For instance, we can implement the above multi-line statement as:
a1 = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a1)

colors = ['red',
          'blue',
          'green']
print(colors)

a2 = 1; b = 2; c = 3
print(a2,b,c)

print()
for i in range(1,11):
    print(i)
    if i == 5:
      break

print()
if True:
    print('Hello')
    a3 = 5

if True: print('Hello'); a4 = 5

'''This is a multi-line comment
And I know it
'''