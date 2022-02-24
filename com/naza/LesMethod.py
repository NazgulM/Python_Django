name = 'Askar'
age = 36
info = 'I live and work in Bishkek'

print(name, '\n', age, '\n')
print(age, end=' ')
print(name, end=' ')
print(info)

# method format
print('Name: {0} \nAge: {1} \nInfo: {2} '.format(name, age, info))
# f string
print(f'Name: {name} \nAge: {age} \nInfo: {info}')
