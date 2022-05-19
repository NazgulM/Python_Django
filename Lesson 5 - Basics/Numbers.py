print(100/2**2)
s = '''hello
world
nazka
aruuke
'''
print(s)
print(len(s))

name = 'Dasha'
mid_name = 'Semenovna'
balance = 32.56
text = '''Dear''' + ' Semen ' + 'Semenovich' + ''' , balance of your account is  ''' + '32.56' + ' Euro'
print(text)

text1 = '''Dear {name} {mid_name},  balance of your account is {balance} Euro '''.format(mid_name
=mid_name, name=name, balance=balance)
print(text1)

word = input()
print('''Что Вы сказали? {word}? Какое интересное слово'''.format(word=word))

print(f'Что Вы сказали? {input()}? Какое интересное слово')

print('Что Вы сказали? {0}? Какое интересное слово'.format(input()))

q=input()
print('Что Вы сказали? %s? Какое интересное слово'%q)


print('''Что Вы сказали? {}? Какое интересное слово'''.format(input()))

a = input()
b = input()
print('''Здравствуйте, {b} {a}!'''.format(b = b, a = a))

print("Здравствуйте, {1} {0}!".format(input(), input()))

name = input()
surname = input()
print('Здравствуйте, {1} {0}!'.format(name, surname))

a = int(input())
print('''Для числа {0} предыдущим будет число {1}.'''.format(a, a-1))
print('''Для числа {0} следующим будет число {1}.'''.format(a, a+1))



message = "Для числа {n} предыдущим будет число {prev}.\nДля числа {n} следующим будет число {next}."
n = int(input())
print(message.format(n=n, prev=n - 1, next=n + 1))