print('hello\nworld\n456')
d = 'hello'
e = 'world'
# Concatenation
print('abc' + 'dec')
print(d + ' ' + e)
print('abc' + str(3))
print(len('abc'))
a = 'Normal practice'
print('You entered', len(a), 'symbols')
b = '@#$4567'
print('4' in b)
print('54' in b)
print('AAA' == 'BBB')
print('a'>'A')
print('zxcv' <= 'asdf')

print('Я стану крутым программистом!\n'*3)

a = 'Я стану крутым программистом!'
print(a,a,a, sep = '\n')

print("""Я стану крутым программистом!
Я стану крутым программистом!
Я стану крутым программистом!""")

n='Я стану крутым программистом!'
print((n+'\n')*3)

print(*['Я стану крутым программистом!' for i in range(3)], sep='\n')

d='Я стану крутым программистом!\n'
print(d*3)

a = 'Я стану крутым программистом!'

for i in range(3):
    print(a)

print('Я стану крутым программистом!\nЯ стану крутым программистом!\nЯ стану крутым программистом!')

print("W"*777)

a = 'WWWWWWW'
print(a*111)

[print('W', end='') for _ in range(777)]

print('Лев Николаевич Толстой написал "Война и мир"')

print("Лев Николаевич Толстой написал \"Война и мир\"")

s = '«Лев Николаевич Толстой написал "Война и мир"»'
print(s[1:-1])

print(input().lstrip("<<").rstrip(">>"))
print(input().replace('«','').replace('»',''))

print(f'{input()}\n{input()}')
print(input(), input(), sep='\n')
print(input()+"\n" + input())
for i in range(2):
    print(input())

[print(_) for _ in [input() for _ in range(2)]]

a, b, c = input(), input(), input()
print(c, b, a, sep='\n')

print("{2}\n{1}\n{0}".format(input(),input(),input()))

l=[ input() for _ in range(3)]
for i in l[::-1]:
    print(i)

print('\n'.join([input() for i in '123'][::-1]))

print((input()+ ' ')*4)

s = input()+' '
print(s*4)

print("{0} {0} {0} {0}".format(input()))

x = input()
print(x,x,x,x,sep = ' ')

print(len(input()))
print(sum([1 for _ in input()]))
a = input()
print(len(a))


a,b = input(), input()
print(b+a)

print("{1}{0}".format(input(), input()))

z = input()
print (input()+z)

print(input()*3)

a,b,c = input().split()
print(f'Simvol code {a} is {ord(a)}.')
print(f'Simvol code {b} is {ord(b)}.')
print(f'Simvol code {c} is {ord(c)}.')

[print(f'Simvol code {el} is {ord(el)}.') for el in input().split()]
a,b,c=map(str,input().split())
print("Simvol code",a,"is",ord(a),end='.\n')
print("Simvol code",b,"is",ord(b),end='.\n')
print("Simvol code",c,"is",ord(c),end='.\n')

chars = input().split()
for c in chars:
    print(f"Simvol code {c} is {ord(c)}.")