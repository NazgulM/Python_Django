print('hello'.upper())
print('Hello'.lower())
print('My name is Nazgul'.count('a'))
print('aruuke Bakai Nursultan'.count('a',0, 10))
print('hello world'.find('ol'))
print('hello world'.rfind('o',6))
print('hello world'.index('o'))
print('Naza'.replace('a', 'aaaa'))
print('hello      world'.replace(' ',''))
print('123456789'.isalpha())
print('nazakachikaaruuke'.isalpha())
print('123456'.isdigit())
print('111'.rjust(5,'2'))
print('222'.ljust(10,'3'))
print('12, 456, 7899'.split(','))
print('hello  \n'.strip())
print('HELLO'.lower().replace('H', 'm'))
# print(input().upper())

print('Helen'.lower().count('e'))

# print(input().lower().replace('w','').replace('z', ''))
#
# print(input().find('a'))
# print(input().rfind('a'))
#
# print(len(input().split()))
#
# print(input().replace(' ', ','))

x = input()
x = x.lower().replace('a', '').replace('o','').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
print('.' + '.'.join(x))

