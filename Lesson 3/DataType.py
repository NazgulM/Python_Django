num_int = 123
num_str = "456"

pnum_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

# Key Points to Remember
# Type Conversion is the conversion of object from one data type to another data type.
# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.
# Explicit Type Conversion is also called Type Casting,
# the data types of objects are converted using predefined functions by the user.
# In Type Casting, loss of data may occur as
# we enforce the object to a specific data type.