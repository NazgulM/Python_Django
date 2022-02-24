name = input('Please enter your name: ')
print(name)
age = input('Enter your age: ')
print(age)
gender = input('Enter your gender: ')
print(gender)
company = input('Enter your company name: ')
print(company)
status = input("Your marital status: ")
print(status)
address = input("Enter your address: ")
print(address)
# length of the name
print(len(name))
# searching an a
print(name.find('a'))
# second index in address
print(address[2])
# print the name from the second letter
print(name[1:])
# print the company in reverse method
print(company[::-1])
# Task 6
print('\nName: {0}\n Age: {1}\n Gender: {2}\n Company: {3}\n Marital status: {4}\n Address: {5} '.format(name, age, gender,  company, status, address))
# method f
print(f'\nEnter your name: {name} \nEnter your age: {age} \nEnter gender: {gender} \nEnter your company name: {company} \nMarital status: {status} \nLiving address: {address}')
# method end
print('\nPlease enter your name: ', name, end=' ')
print('\nEnter your age: ', age, end=' ')
print('\nEnter your gender: ', gender, end=' ')
print('\nEnter your company name: : ', company, end=' ')
print('\nEnter your marital status: ', status, end=' ')
print('\nEnter your living address: ', address, end=' ')
