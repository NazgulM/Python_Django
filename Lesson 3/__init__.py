a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[2] = 4
print(a)

# Python Tuple
# Tuple is an ordered sequence of items same as a list.
# The only difference is that tuples are immutable.
# Tuples once created cannot be modified.
# Tuples are used to write-protect data and are usually faster
# than lists as they cannot change dynamically.
# It is defined within parentheses () where items are separated by commas.

t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10

s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
# s[5] ='d'

# Python Set
# Set is an unordered collection of unique items.
# Set is defined by values separated by comma inside braces { }.
# Items in a set are not ordered.

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

a = {1,2,2,3,3,3}
print(a)

# hon Dictionary
# Dictionary is an unordered collection of key-value pairs.
# It is generally used when we have a huge amount of data.
# Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.
# In Python, dictionaries are defined within braces {} with each
# item being a pair in the form key:value. Key and value can be of any type.
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

